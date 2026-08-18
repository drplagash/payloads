#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path.cwd()
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
MIPS_SHA = "cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41"


def run(*args: str, check: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=check)


def git_mv(src: str, dst: str) -> None:
    s = ROOT / src
    d = ROOT / dst
    if s.exists():
        d.parent.mkdir(parents=True, exist_ok=True)
        run("git", "mv", src, dst)


def rm_path(path: str) -> None:
    p = ROOT / path
    if p.exists():
        run("git", "rm", "-r", path)


def write(path: str, text: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + "\n", encoding="utf-8")


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


def first_nonempty_line(path: Path, limit: int = 220) -> str:
    text = read(path)
    for line in text.splitlines():
        line = line.strip()
        if line:
            return line[:limit]
    return "Sin preview disponible."


def extract_ioc_summary(path: Path) -> str:
    text = read(path)
    if not text:
        return "IOCs no disponibles"
    ips = sorted(set(re.findall(r"\b(?:\d{1,3}\[\.\]|\d{1,3}\.)(?:\d{1,3}\[\.\]|\d{1,3}\.)(?:\d{1,3}\[\.\]|\d{1,3}\.)(?:XXX|\d{1,3})\b", text)))
    urls = sorted(set(re.findall(r"hxxps?://[^\s\"'<>]+", text)))
    bits = []
    if ips:
        bits.append("IPs: " + ", ".join(ips[:6]))
    if urls:
        bits.append("URLs: " + ", ".join(urls[:4]))
    return "; ".join(bits) if bits else "IOCs en archivo defangueado"


def evidence_flags(base: Path) -> list[str]:
    flags = []
    if (base / "evidence" / "commands.defanged.txt").exists():
        flags.append("comandos")
    if (base / "evidence" / "iocs.defanged.json").exists():
        flags.append("IOCs")
    if (base / "metadata" / "metadata.json").exists():
        flags.append("metadata")
    if (base / "detections.md").exists():
        flags.append("detecciones")
    return flags or ["review"]


def rewrite_payload_readmes() -> None:
    base = ROOT / "payloads" / "detectados"
    if not base.exists():
        return
    rows = []
    for d in sorted(p for p in base.iterdir() if p.is_dir() and SHA_RE.match(p.name)):
        cmd_path = d / "evidence" / "commands.defanged.txt"
        ioc_path = d / "evidence" / "iocs.defanged.json"
        det_path = d / "detections.md"
        preview = first_nonempty_line(cmd_path)
        iocs = extract_ioc_summary(ioc_path)
        ev = evidence_flags(d)
        write(str(d.relative_to(ROOT) / "README.md"), f"""
# {d.name}

Payload/artifact detectado por T-Pot y publicado para revisión humana.

## Resumen

| Campo | Valor |
|---|---|
| SHA256 | `{d.name}` |
| Origen | T-Pot / Oraculo SOC |
| Estado | detectado high-signal |
| Evidencia | {", ".join(ev)} |

## Comando o payload observado

```text
{preview}
```

## Direcciones e IOCs

```text
{iocs}
```

## Archivos útiles

- `evidence/commands.defanged.txt`: comandos/payload HTTP observados, defangueados.
- `evidence/iocs.defanged.json`: IOCs asociados, defangueados.
- `metadata/metadata.json`: metadata preservada del análisis.
- `detections.md`: notas de detección cuando existían en el review original.

## Lectura defensiva

Esto no se publica como adorno ni como hash suelto. Se publica porque contiene señal útil para hunting: comandos, descarga remota, staging, ejecución, IOCs, metadata o detecciones.

No ejecutar nada. Todo material operativo debe tratarse como evidencia defensiva inerte.
""")
        rows.append((d.name, ", ".join(ev), preview.replace("|", "\\|")))

    lines = [
        "# Payloads detectados",
        "",
        "Listado visible de payloads/artifacts detectados por firma SHA256.",
        "",
        f"Total publicado: **{len(rows)}**",
        "",
        "Cada entrada abre en una carpeta con README humano, comandos observados, IOCs, metadata y detecciones cuando existían.",
        "",
        "| Firma / SHA256 | Evidencia | Preview |",
        "|---|---|---|",
    ]
    for sha, ev, preview in rows:
        lines.append(f"| [`{sha}`]({sha}/) | {ev} | `{preview[:170]}` |")
    write("payloads/detectados/README.md", "\n".join(lines))


def main() -> None:
    # Mover lo que sí debe verse.
    git_mv("firmas/high-signal", "payloads/detectados")
    git_mv(f"firmas/{MIPS_SHA}", f"malware/{MIPS_SHA}")
    git_mv("casos/tpot-router-downloader-campaign-91-92-40", "casos/router-downloader-91-92-40")

    # Mover detecciones útiles a donde tienen contexto.
    git_mv("detecciones/router-downloader-91-92-40.md", "casos/router-downloader-91-92-40/detecciones.md")
    git_mv("detecciones/mips-cad9e90-yara.md", f"malware/{MIPS_SHA}/detecciones.md")

    # Sacar el caso MIPS flojo. El MIPS vive en malware, donde corresponde.
    rm_path("casos/tpot-mips-payload-cad9e90")

    # Sacar ruido de la cara pública. Git lo conserva en historia; main queda humano.
    for path in [
        "assets", "docs", "showcase", "hallazgos", "intel", "detecciones", "firmas",
        "CATALOG.jsonl", "INDEX.md", "DISCLAIMER.md",
        "tools/publish_high_signal.py", "tools/restructure_public_tree.py", "tools",
    ]:
        rm_path(path)

    rewrite_payload_readmes()

    write("README.md", """
# Payloads

Repositorio público de Oraculo SOC para mostrar payloads, malware y casos derivados de T-Pot.

Acá se entra para ver evidencia, no para hacer arqueología entre carpetas vacías. Increíblemente, esa es una mejora técnica.

## Entrar directo

| Quiero ver | Entrar acá |
|---|---|
| Payloads detectados por firma | [`payloads/detectados/`](payloads/detectados/) |
| Malware confirmado | [`malware/`](malware/) |
| Casos explicados | [`casos/`](casos/) |

## Qué hay publicado

| Área | Cantidad | Qué muestra |
|---|---:|---|
| Payloads detectados | 517 | Artifacts high-signal de T-Pot con comandos, IOCs, metadata y detecciones cuando existían |
| Malware confirmado | 1 | Muestra ELF32 MIPS con evidencia, análisis, metadata, raw inerte y YARA |
| Casos explicados | 1 | Campaña router/IoT downloader con superficies atacadas y detecciones |

## Lectura rápida

Primero abrí [`payloads/detectados/`](payloads/detectados/). Ahí está el listado visible por firma.

Al hacer clic en una firma se ve:

- comando o payload observado,
- direcciones e IOCs defangueados,
- metadata,
- detecciones si existían,
- archivos de evidencia.

Después abrí [`malware/`](malware/) para ver las muestras confirmadas como malware/payload binario.

Finalmente abrí [`casos/`](casos/) para ver ejemplos explicados como informe.

## Seguridad

Material publicado para investigación defensiva, SOC, CTI y laboratorio controlado. No ejecutar muestras ni comandos capturados. Los IOCs y comandos se publican defangueados cuando corresponde.
""")

    write("payloads/README.md", """
# Payloads

Payloads y artifacts detectados por T-Pot, publicados por firma.

## Listado principal

- [`detectados/`](detectados/): 517 payloads/artifacts high-signal visibles.

Cada entrada tiene README humano y evidencia asociada.
""")

    write("malware/README.md", f"""
# Malware

Muestras confirmadas o promovidas como malware/payload binario.

## Confirmadas

| Firma / SHA256 | Tipo | Entrada |
|---|---|---|
| `{MIPS_SHA}` | ELF32 MIPS payload / malware-like artifact | [`{MIPS_SHA}/`]({MIPS_SHA}/) |

## Regla

Esta carpeta no es para candidatos flojos. Acá van muestras con evidencia suficiente: análisis, metadata, IOCs, raw inerte y detecciones/YARA cuando existan.
""")

    write("casos/README.md", """
# Casos

Casos explicados como historia técnica. No son hashes sueltos.

## Publicados

| Caso | Qué muestra |
|---|---|
| [`router-downloader-91-92-40`](router-downloader-91-92-40/) | Campaña router/IoT downloader agrupada desde 517 artifacts high-signal. Incluye abuso de HNAP, JNAP, Netgear setup.cgi, ping_test, syscmd.htm, ttcp_ip y weblogin.cgi. |

El caso MIPS se retiró de acá porque como caso era débil. Vive en `malware/`, donde corresponde.
""")

    # Actualizar índice del caso con paths nuevos.
    case_firmas = ROOT / "casos" / "router-downloader-91-92-40" / "firmas.md"
    if case_firmas.exists():
        text = case_firmas.read_text(encoding="utf-8", errors="replace")
        text = text.replace("../../firmas/high-signal/", "../../payloads/detectados/")
        text = text.replace("firmas/high-signal/", "payloads/detectados/")
        case_firmas.write_text(text, encoding="utf-8")

    print("PUBLIC_TREE=payloads_malware_casos")
    print("PAYLOADS_VISIBLE_DIRS=", len([p for p in (ROOT / "payloads" / "detectados").iterdir() if p.is_dir()]))
    print("NEXT=git status --short && git add -A && git commit -m 'Simplify public tree around payloads and malware' && git push origin main")


if __name__ == "__main__":
    main()
