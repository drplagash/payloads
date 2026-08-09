# 🧬 Payload Analysis

`28b2dfd8d920df83388ca9bc07236319f7a075627a317629ef6861c1ba8eec85`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:05:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `28b2dfd8d920df83388ca9bc07236319f7a075627a317629ef6861c1ba8eec85`
- **SHA1:** `0df85356ec0a2c54d860e17a5307292cf45b2e70`
- **MD5:** `8c2dabc7200b754aba0f210a8f48d64d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 357 B |
| Entropía | 4.77 |
| Strings | 12 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 28b2dfd8d920df83388ca9bc07236319f7a075627a317629ef6861c1ba8eec85 | static_analysis |
| ip | 36.32.156.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
