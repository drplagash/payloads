# 🧬 Payload Analysis

`d2960a3e1ce80bb53f45c13379fbacb9d8d36dae777f593d2a0ceebc15e01af0`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:49:32+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d2960a3e1ce80bb53f45c13379fbacb9d8d36dae777f593d2a0ceebc15e01af0`
- **SHA1:** `289e6f6ef1287791dd347f2685aa21beca657aac`
- **MD5:** `37434e5e66c17106264eafdf3135506d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.33 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://lists[.]wikimedia[.]org/mailm | strings |
| url | hxxps://www[.]mediawiki[.]org/wiki/Special:MyLanguage/Manual:Configuration_settings | strings |
| url | hxxps://www[.]mediawiki[.]org/wiki/Special:MyLanguage/Manual:FAQ | strings |
| hash | d2960a3e1ce80bb53f45c13379fbacb9d8d36dae777f593d2a0ceebc15e01af0 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
