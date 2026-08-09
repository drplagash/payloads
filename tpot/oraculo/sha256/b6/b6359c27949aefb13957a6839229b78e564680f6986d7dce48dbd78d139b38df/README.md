# 🧬 Payload Analysis

`b6359c27949aefb13957a6839229b78e564680f6986d7dce48dbd78d139b38df`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:10:14.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b6359c27949aefb13957a6839229b78e564680f6986d7dce48dbd78d139b38df`
- **SHA1:** `19e2f1281c4edb09cddd1a67c99269085c4ca893`
- **MD5:** `199362f90db471e14b3af2070b1152da`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 710 B |
| Entropía | 5.34 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://www[.]reddit[.]com/r/sportsbook/ | strings |
| url | hxxps://alfabienes[.]com[.]co/category/megaways/california/king88/61683 | strings |
| hash | b6359c27949aefb13957a6839229b78e564680f6986d7dce48dbd78d139b38df | static_analysis |
| ip | 180.93.109.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
