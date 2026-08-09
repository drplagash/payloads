# 🧬 Payload Analysis

`afbee1147296692d196bd859b856c52146a1bb7f23e98d9cecec541523ee273f`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:06:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `afbee1147296692d196bd859b856c52146a1bb7f23e98d9cecec541523ee273f`
- **SHA1:** `99450d0ba059424b261244c8b124ca7c27456000`
- **MD5:** `07419a0e82685dbefff8ecba7f2b8ee0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (338) |
| Tamaño | 627 B |
| Entropía | 5.09 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (338); iocs=6

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2004/08/addressing | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2005/04/discovery | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2005/04/discovery/Probe | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2006/02/devprof | strings |
| url | hxxp://www[.]w3[.]org/2003/05/soap-envelope | strings |
| hash | afbee1147296692d196bd859b856c52146a1bb7f23e98d9cecec541523ee273f | static_analysis |
| ip | 146.88.241.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
