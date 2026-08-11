# 🧬 Payload Analysis

`0064dc3c1e193673661fe9401b8d725a9a0ae85dc056f44dfbc307a6daafe8e2`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificaron 4 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/0064dc3c1e193673661fe9401b8d725a9a0ae85dc056f44dfbc307a6daafe8e2.md](../../../../../malware-like/oraculo/botnet/0064dc3c1e193673661fe9401b8d725a9a0ae85dc056f44dfbc307a6daafe8e2.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:08:22.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0064dc3c1e193673661fe9401b8d725a9a0ae85dc056f44dfbc307a6daafe8e2`
- **SHA1:** `b68b7529a87ca7a6c233094dba67fb5d1c41ddec`
- **MD5:** `867157a70d4b8f0d56f3e6f2bfe0266e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 891 B |
| Entropía | 5.53 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://t[.]me/ | strings |
| url | hxxps://alfabienes[.]com[.]co/download/parlay-app-88vip-v6.10?ref=17052497c5b7&_=1782129098061 | strings |
| url | hxxp://www[.]google[.]com/bot.html) | strings |
| hash | 0064dc3c1e193673661fe9401b8d725a9a0ae85dc056f44dfbc307a6daafe8e2 | static_analysis |
| ip | 180.93.109.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
