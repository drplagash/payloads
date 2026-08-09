# 🧬 Payload Analysis

`abade9c7b02910f1c6de354744928f5a0b47babee48f23455cba2eec6f03bbaa`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:10:14+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `abade9c7b02910f1c6de354744928f5a0b47babee48f23455cba2eec6f03bbaa`
- **SHA1:** `fc3d7e50c17d8ed2aeb1085765ff78c728be0624`
- **MD5:** `c79890765cf9a93e9112d63d7b2630b1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 923 B |
| Entropía | 5.5 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 126.0.0.XXX | static_analysis |
| url | hxxp://www[.]google[.]com/bot.html) | strings |
| url | hxxps://alfabienes[.]com[.]co/tag/wagering-7d747a-casino/page/135/?s=wagering&post_type=product&lang=en | strings |
| url | hxxps://www[.]reddit[.]com/r/gambling/ | strings |
| hash | abade9c7b02910f1c6de354744928f5a0b47babee48f23455cba2eec6f03bbaa | static_analysis |
| ip | 180.93.109.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
