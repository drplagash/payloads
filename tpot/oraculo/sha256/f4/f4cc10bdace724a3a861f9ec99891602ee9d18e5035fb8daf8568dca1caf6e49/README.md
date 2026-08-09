# 🧬 Payload Analysis

`f4cc10bdace724a3a861f9ec99891602ee9d18e5035fb8daf8568dca1caf6e49`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f4cc10bdace724a3a861f9ec99891602ee9d18e5035fb8daf8568dca1caf6e49`
- **SHA1:** `e40133ddbd4eec0ffebadd44d9448edd9afcb85f`
- **MD5:** `0a0ffb3fe91d3217480a23ee1ea272eb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF, LF line terminators |
| Tamaño | 813 B |
| Entropía | 5.37 |
| Strings | 27 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF, LF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2002/04/secext | strings |
| hash | f4cc10bdace724a3a861f9ec99891602ee9d18e5035fb8daf8568dca1caf6e49 | static_analysis |
| ip | 185.16.38.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
