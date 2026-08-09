# 🧬 Payload Analysis

`69e64047badd56742a91e82fa56e6b808788d3863b910f109a338fc0aa4ffb71`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `69e64047badd56742a91e82fa56e6b808788d3863b910f109a338fc0aa4ffb71`
- **SHA1:** `c5e3cc39cf24aa258fb28158e7d4a72d4db8e120`
- **MD5:** `9a2136c3379b9f51e7adeb3c1bc0a2ff`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 803 B |
| Entropía | 5.5 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 143.164.202.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 69e64047badd56742a91e82fa56e6b808788d3863b910f109a338fc0aa4ffb71 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
