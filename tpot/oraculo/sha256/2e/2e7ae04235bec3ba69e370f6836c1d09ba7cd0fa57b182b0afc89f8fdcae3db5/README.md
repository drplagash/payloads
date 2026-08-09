# 🧬 Payload Analysis

`2e7ae04235bec3ba69e370f6836c1d09ba7cd0fa57b182b0afc89f8fdcae3db5`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:58:35+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2e7ae04235bec3ba69e370f6836c1d09ba7cd0fa57b182b0afc89f8fdcae3db5`
- **SHA1:** `36cb31081651308b0c281656042315c814fc49e5`
- **MD5:** `c01c4b40c3e689e020022d2d776150bf`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (712), with CRLF line terminators |
| Tamaño | 866 B |
| Entropía | 5.34 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (712), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 196.251.121.XXX | static_analysis |
| url | hxxp://196.251.121.XXX/a3f8d2/adb.sh; | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| hash | 2e7ae04235bec3ba69e370f6836c1d09ba7cd0fa57b182b0afc89f8fdcae3db5 | static_analysis |
| ip | 115.84.178.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
