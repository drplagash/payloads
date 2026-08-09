# 🧬 Payload Analysis

`e43423452b562b8214c6b560cc830ceb5cf44a89c3687e51171595f525e2106b`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificaron 5 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:08:22.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e43423452b562b8214c6b560cc830ceb5cf44a89c3687e51171595f525e2106b`
- **SHA1:** `2051ac39a018aafefae0d491bbbe1a486796ef3a`
- **MD5:** `5ea46d70f997e55889595efe115ccf7a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 887 B |
| Entropía | 5.51 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://t[.]me/ | strings |
| url | hxxp://www[.]google[.]com/bot.html) | strings |
| url | hxxps://alfabienes[.]com[.]co/search?q=88gold+in+sweden+max88&location=sweden&page=443 | strings |
| ip | 126.0.0.XXX | static_analysis |
| hash | e43423452b562b8214c6b560cc830ceb5cf44a89c3687e51171595f525e2106b | static_analysis |
| ip | 180.93.109.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
