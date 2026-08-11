# 🧬 Payload Analysis

`c10c91cd8a10f9d6618383a4be439f03d816af49b154358e5b4fc2bbd13965b4`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificaron 4 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/c10c91cd8a10f9d6618383a4be439f03d816af49b154358e5b4fc2bbd13965b4.md](../../../../../malware-like/oraculo/botnet/c10c91cd8a10f9d6618383a4be439f03d816af49b154358e5b4fc2bbd13965b4.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:08:22.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c10c91cd8a10f9d6618383a4be439f03d816af49b154358e5b4fc2bbd13965b4`
- **SHA1:** `3e5814928bfba50e46891a9cca3e234c596f1c5a`
- **MD5:** `edef2805145e6577590732fb3d2b7c31`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 934 B |
| Entropía | 5.56 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://alfabienes[.]com[.]co/search?q=pragmatic%20play+no%20deposit&sort=popularity&order=asc&limit=773&_=1782128774390 | strings |
| url | hxxps://www[.]facebook[.]com/ | strings |
| url | hxxp://www[.]google[.]com/bot.html) | strings |
| hash | c10c91cd8a10f9d6618383a4be439f03d816af49b154358e5b4fc2bbd13965b4 | static_analysis |
| ip | 180.93.109.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
