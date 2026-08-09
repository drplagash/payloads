# 🧬 Payload Analysis

`d32b3d55f6f9dc9f6c7bd7340d7f6c0e10eaee963bfc837d1e399767e6c87994`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:22:21+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d32b3d55f6f9dc9f6c7bd7340d7f6c0e10eaee963bfc837d1e399767e6c87994`
- **SHA1:** `99cac2af8bec2980ca593b7b4cb12112656c88ed`
- **MD5:** `1546d0d2c92e711fd202877512393179`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (704), with CRLF line terminators |
| Tamaño | 858 B |
| Entropía | 5.32 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (704), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 176.65.149.XXX | static_analysis |
| url | hxxp://176.65.149.XXX/adb.sh; | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| hash | d32b3d55f6f9dc9f6c7bd7340d7f6c0e10eaee963bfc837d1e399767e6c87994 | static_analysis |
| ip | 39.104.63.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
