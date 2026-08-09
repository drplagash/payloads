# 🧬 Payload Analysis

`8e72c4b2dbdc3fa9fc02ef460000c010e304b880b8b3ff728ddb81f3c9e9234d`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:18:27+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8e72c4b2dbdc3fa9fc02ef460000c010e304b880b8b3ff728ddb81f3c9e9234d`
- **SHA1:** `e311782d301b9333030aa22f4abffa6346ad3607`
- **MD5:** `24632f7dfba1a3bc3ed32f0aaba82aff`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (696), with CRLF line terminators |
| Tamaño | 850 B |
| Entropía | 5.32 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (696), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 212.7.202.XXX | static_analysis |
| url | hxxp://212.7.202.XXX:2025/adb; | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| hash | 8e72c4b2dbdc3fa9fc02ef460000c010e304b880b8b3ff728ddb81f3c9e9234d | static_analysis |
| ip | 51.158.97.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
