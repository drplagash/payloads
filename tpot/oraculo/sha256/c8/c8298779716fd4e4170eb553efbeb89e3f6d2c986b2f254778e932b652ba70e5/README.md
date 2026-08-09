# 🧬 Payload Analysis

`c8298779716fd4e4170eb553efbeb89e3f6d2c986b2f254778e932b652ba70e5`

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

- **SHA256:** `c8298779716fd4e4170eb553efbeb89e3f6d2c986b2f254778e932b652ba70e5`
- **SHA1:** `b78246468ac44357a971c5e778af8b8ef7c11fc5`
- **MD5:** `17854d46a529a5f783b3032cf0736bff`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 908 B |
| Entropía | 5.54 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]google[.]com/bot.html) | strings |
| url | hxxps://www[.]google[.]com/ | strings |
| url | hxxps://alfabienes[.]com[.]co/?s=deposit%20bonus+claim%20bonus+sportsbook&page=204&ref=8090e6799f96 | strings |
| hash | c8298779716fd4e4170eb553efbeb89e3f6d2c986b2f254778e932b652ba70e5 | static_analysis |
| ip | 180.93.109.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
