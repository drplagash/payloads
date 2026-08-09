# 🧬 Payload Analysis

`0b128463615fb7fa12d026561e1ad68f7fe50dd8b5245ce8ac2bc59e092fbe15`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:56:43+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0b128463615fb7fa12d026561e1ad68f7fe50dd8b5245ce8ac2bc59e092fbe15`
- **SHA1:** `01851420ed1b208be9959c6c87685d63c388037a`
- **MD5:** `2de8872953e9771efcce16ac8d646c20`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 176 B |
| Entropía | 5.1 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.144.XXX | static_analysis |
| url | hxxp://www[.]google[.]com/bot.html) | strings |
| hash | 0b128463615fb7fa12d026561e1ad68f7fe50dd8b5245ce8ac2bc59e092fbe15 | static_analysis |
| ip | 64.236.142.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
