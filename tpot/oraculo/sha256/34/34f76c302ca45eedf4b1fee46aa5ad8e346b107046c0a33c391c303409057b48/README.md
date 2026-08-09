# 🧬 Payload Analysis

`34f76c302ca45eedf4b1fee46aa5ad8e346b107046c0a33c391c303409057b48`

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

- **SHA256:** `34f76c302ca45eedf4b1fee46aa5ad8e346b107046c0a33c391c303409057b48`
- **SHA1:** `d4a4b0c469bd63ea5fcf50092a03ef5fd4c67c07`
- **MD5:** `f8cbbf2f4452a49f1ed154526fafb7a1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 903 B |
| Entropía | 5.54 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]google[.]com/bot.html) | strings |
| url | hxxps://alfabienes[.]com[.]co/review/casino-gold88-casino-5c0dac25?ref=ac4777901354&_=1782085526319 | strings |
| url | hxxps://t[.]me/ | strings |
| hash | 34f76c302ca45eedf4b1fee46aa5ad8e346b107046c0a33c391c303409057b48 | static_analysis |
| ip | 180.93.109.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
