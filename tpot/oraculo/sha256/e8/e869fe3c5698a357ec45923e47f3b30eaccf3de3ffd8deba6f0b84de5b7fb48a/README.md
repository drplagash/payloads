# 🧬 Payload Analysis

`e869fe3c5698a357ec45923e47f3b30eaccf3de3ffd8deba6f0b84de5b7fb48a`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:08:59+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e869fe3c5698a357ec45923e47f3b30eaccf3de3ffd8deba6f0b84de5b7fb48a`
- **SHA1:** `33f4dba89c7e06593de5d1e3bbd5a386c7496a72`
- **MD5:** `716063911b07485b2639a5797d078afa`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 778 B |
| Entropía | 5.44 |
| Strings | 20 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 66.249.155.XXX | static_analysis |
| url | hxxp://www[.]google[.]com/bot.html) | strings |
| url | hxxps://alfabienes[.]com[.]co/casino | strings |
| url | hxxps://www[.]google[.]com/ | strings |
| hash | e869fe3c5698a357ec45923e47f3b30eaccf3de3ffd8deba6f0b84de5b7fb48a | static_analysis |
| ip | 180.93.109.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
