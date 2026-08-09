# 🧬 Payload Analysis

`3e7fc012980608be7b6b23d926e6b0d3759e813a6deba7857b4f15c1cf808ac5`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:08:22.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3e7fc012980608be7b6b23d926e6b0d3759e813a6deba7857b4f15c1cf808ac5`
- **SHA1:** `d20f5c3de0f70183ad2626ac2b41f8968a20a721`
- **MD5:** `6d7ced6d783122607f2f20a7fcc0bf3c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 701 B |
| Entropía | 5.36 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://www[.]bing[.]com/tk?url=hxxps://alfabienes[.]com[.]co/f8bet-978782 | strings |
| url | hxxps://www[.]pinterest[.]com/ | strings |
| hash | 3e7fc012980608be7b6b23d926e6b0d3759e813a6deba7857b4f15c1cf808ac5 | static_analysis |
| ip | 180.93.109.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
