# 🧬 Payload Analysis

`4df91988f8d7d3cbe49d668b03cd0bce72cdead18eabd573c1624a3535423b7a`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:08:22+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4df91988f8d7d3cbe49d668b03cd0bce72cdead18eabd573c1624a3535423b7a`
- **SHA1:** `2cc2ab8967b7ae07d59cf64b1e12c4b7b82ec928`
- **MD5:** `84f265430bf5176c2fe1b1461f2cc59c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 913 B |
| Entropía | 5.53 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]google[.]com/bot.html) | strings |
| url | hxxps://alfabienes[.]com[.]co/bonus/vip88-no-deposit-896-d632?ref=1c56b89860f6&_=1782128882496 | strings |
| url | hxxps://www[.]facebook[.]com/groups/ | strings |
| hash | 4df91988f8d7d3cbe49d668b03cd0bce72cdead18eabd573c1624a3535423b7a | static_analysis |
| ip | 180.93.109.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
