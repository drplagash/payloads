# 🧬 Payload Analysis

`0886be79883022c43807d846982c50913aca0749a891d0b9d0d0dce23e07b0a8`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:37:42+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0886be79883022c43807d846982c50913aca0749a891d0b9d0d0dce23e07b0a8`
- **SHA1:** `6b3f36a768ac7d40aa469b39b11a1c0cc25e68b1`
- **MD5:** `f623f530280ab8b265fe68951a46998a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.29 |
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
| hash | 0886be79883022c43807d846982c50913aca0749a891d0b9d0d0dce23e07b0a8 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
