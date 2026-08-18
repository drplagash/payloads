#!/usr/bin/env python3
from pathlib import Path
import re
import shutil
import sys

ROOT = Path.cwd()
LEGACY = ROOT.parent / "payloads-legacy-bulk" / "review" / "legacy-sha256-useful-review"
CANDIDATES = Path("/tmp/tpot-high-signal-candidates.txt")


def fail(msg: str) -> None:
    print(msg, file=sys.stderr)
    raise SystemExit(1)


def defang(text: str) -> str:
    text = text.replace("http://", "hxxp://").replace("https://", "hxxps://")
    text = re.sub(r"(?<=\d)\.(?=\d)", "[.]", text)
    text = re.sub(r"([A-Za-z0-9-]+)\.([A-Za-z]{2,})(?=[/:\\s]|$)", r"\1[.]\2", text)
    return text


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def safe_copy_text(src: Path, dst: Path, do_defang: bool = True) -> bool:
    if not src.exists() or not src.is_file():
        return False
    text = read_text(src)
    if do_defang:
        text = defang(text)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text, encoding="utf-8")
    return True


def load_candidates() -> list[str]:
    if not CANDIDATES.exists() or CANDIDATES.stat().st_size == 0:
        fail("NO_EXISTE_/tmp/tpot-high-signal-candidates.txt")

    shas = []
    for line in CANDIDATES.read_text(encoding="utf-8", errors="replace").splitlines():
        sha = line.strip().lower()
        if re.fullmatch(r"[0-9a-f]{64}", sha):
            shas.append(sha)
    shas = sorted(set(shas))
    if not shas:
        fail("NO_SHA_CANDIDATES")
    return shas


def first_preview(text: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line:
            return line[:240]
    return "High-signal T-Pot artifact preserved from legacy review."


def main() -> None:
    if ROOT.name != "payloads":
        fail("Ejecutar desde ~/payloads")
    if not LEGACY.exists():
        fail(f"NO_EXISTE_LEGACY={LEGACY}")

    shas = load_candidates()
    out_base = ROOT / "firmas" / "high-signal"
    out_base.mkdir(parents=True, exist_ok=True)

    rows = []

    for sha in shas:
        src = LEGACY / sha
        dst = out_base / sha
        evdir = dst / "evidence"
        metadir = dst / "metadata"
        evdir.mkdir(parents=True, exist_ok=True)
        metadir.mkdir(parents=True, exist_ok=True)

        evidence = []

        commands = src / "commands.txt"
        if safe_copy_text(commands, evdir / "commands.defanged.txt", True):
            evidence.append("commands")

        iocs = src / "iocs.json"
        if safe_copy_text(iocs, evdir / "iocs.defanged.json", True):
            evidence.append("iocs")

        metadata = src / "metadata.json"
        if metadata.exists() and metadata.is_file():
            shutil.copyfile(metadata, metadir / "metadata.json")
            evidence.append("metadata")

        detections = src / "detections.md"
        if safe_copy_text(detections, dst / "detections.md", True):
            evidence.append("detections")

        preview = "High-signal T-Pot artifact preserved from legacy review."
        if commands.exists() and commands.is_file():
            preview = first_preview(defang(read_text(commands)))

        evidence_text = ", ".join(evidence) if evidence else "review"

        readme = f"""# {sha}

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `{sha}` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | {evidence_text} |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
{preview}
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
"""
        (dst / "README.md").write_text(readme, encoding="utf-8")
        rows.append((sha, evidence_text, preview.replace("|", "\\|")))

    index = [
        "# High-signal signatures",
        "",
        "Visible published list of high-signal T-Pot artifacts.",
        "",
        f"Total published artifacts: **{len(rows)}**",
        "",
        "| SHA256 | Evidence | Preview |",
        "|---|---|---|",
    ]
    for sha, evidence_text, preview in rows:
        index.append(f"| [`{sha}`]({sha}/) | {evidence_text} | `{preview[:160]}` |")
    index.append("")
    index.append("These are not raw random hashes. They are artifacts promoted into the visible tree because they carried defensive signal.")
    (out_base / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")

    firmas = ROOT / "firmas" / "README.md"
    firmas.write_text(f"""# Firmas

Listado humano de payloads, malware y artifacts high-signal observados por Oraculo SOC.

## Publicado y visible

| Grupo | Cantidad | Entrada |
|---|---:|---|
| High-signal T-Pot artifacts | {len(rows)} | [`high-signal/`](high-signal/) |
| Payloads confirmados completos | 1 | [`cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/`](cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/) |

## Qué es una firma

Una firma puede ser:

- un binario confirmado,
- un payload HTTP,
- un downloader,
- un comando de explotación,
- un artifact útil para detección,
- evidencia con IOCs, metadata o detecciones.

## Confirmada completa

| Firma / SHA256 | Tipo | Resumen |
|---|---|---|
| [`cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41`](cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/) | ELF32 MIPS payload / malware-like artifact | Capturado desde honeypot controlado y promovido con evidencia, metadata, IOCs, raw inerte, análisis y YARA |

## Campañas con firmas agrupadas

| Campaña | Firmas |
|---|---:|
| [`tpot-router-downloader-campaign-91-92-40`](../casos/tpot-router-downloader-campaign-91-92-40/firmas.md) | {len(rows)} |

## Regla

Nada de hash spam sin contexto.

Pero el volumen útil tiene que estar publicado y visible.
""", encoding="utf-8")

    case_sig = ROOT / "casos" / "tpot-router-downloader-campaign-91-92-40" / "firmas.md"
    case_lines = [
        "# Firmas observadas en la campaña",
        "",
        "Listado visible de artifacts high-signal asociados a la campaña router/IoT downloader.",
        "",
        f"Total publicado: **{len(rows)}**",
        "",
        "| SHA256 | Carpeta publicada | Evidence |",
        "|---|---|---|",
    ]
    for sha, evidence_text, _ in rows:
        case_lines.append(f"| `{sha}` | [`firmas/high-signal/{sha}`](../../firmas/high-signal/{sha}/) | {evidence_text} |")
    case_sig.write_text("\n".join(case_lines) + "\n", encoding="utf-8")

    readme = ROOT / "README.md"
    s = readme.read_text(encoding="utf-8")
    if "Firmas high-signal publicadas" not in s:
        s = s.replace(
            "## Firma confirmada",
            f"## Firmas high-signal publicadas\n\n- [`{len(rows)} artifacts high-signal`](firmas/high-signal/) publicados como carpetas visibles.\n\nCada carpeta tiene README humano y evidencia defangueada cuando está disponible.\n\n## Firma confirmada",
        )
    readme.write_text(s, encoding="utf-8")

    print(f"PUBLISHED_HIGH_SIGNAL={len(rows)}")


if __name__ == "__main__":
    main()
