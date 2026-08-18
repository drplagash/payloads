# 🧬 Payload Analysis

`951751e362e4bf856f728a147b93fc543f2ca667111cd5fe2c13c60164ccb16c`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificaron 4 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/951751e362e4bf856f728a147b93fc543f2ca667111cd5fe2c13c60164ccb16c.md](../../../../../malware-like/oraculo/botnet/951751e362e4bf856f728a147b93fc543f2ca667111cd5fe2c13c60164ccb16c.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:10:14.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `951751e362e4bf856f728a147b93fc543f2ca667111cd5fe2c13c60164ccb16c`
- **SHA1:** `64374a359f498428d7dfb4a6335553fd21b2b4d5`
- **MD5:** `0aaa528c28d0c663e406b72f968a5e18`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 990 B |
| Entropía | 5.54 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://www[.]bing[.]com/search?q=gambling+online+asia+88 | strings |
| url | hxxps://alfabienes[.]com[.]co/api/v2/products?search=bookmaker&category=490&tag=bookmaker&page=957&per_page=711&orderby=id&_=1782095813222 | strings |
| url | hxxp://www[.]google[.]com/bot.html) | strings |
| hash | 951751e362e4bf856f728a147b93fc543f2ca667111cd5fe2c13c60164ccb16c | static_analysis |
| ip | 180.93.109.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
