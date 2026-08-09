# 🧬 Payload Analysis

`418586e3b42067462c7b6fbee35f2f83183543c4ad1a0a280b3e0929b49295a5`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:09:37.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `418586e3b42067462c7b6fbee35f2f83183543c4ad1a0a280b3e0929b49295a5`
- **SHA1:** `9212dfffc29ee2527b70419cfb2f87778f29a6a9`
- **MD5:** `3349040f4ac835b1afaa1f9c3413679b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 936 B |
| Entropía | 5.52 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]google[.]com/bot.html) | strings |
| url | hxxps://www[.]google[.]com/search?q=gambling+online+bonus | strings |
| url | hxxps://alfabienes[.]com[.]co/download/bookies-app-12bet-v9.1?ref=3e194fc95fb8&_=1782085567066 | strings |
| hash | 418586e3b42067462c7b6fbee35f2f83183543c4ad1a0a280b3e0929b49295a5 | static_analysis |
| ip | 180.93.109.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
