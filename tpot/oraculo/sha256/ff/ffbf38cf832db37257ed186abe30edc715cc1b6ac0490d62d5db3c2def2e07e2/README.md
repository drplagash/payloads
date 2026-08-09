# 🧬 Payload Analysis

`ffbf38cf832db37257ed186abe30edc715cc1b6ac0490d62d5db3c2def2e07e2`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:34:59+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ffbf38cf832db37257ed186abe30edc715cc1b6ac0490d62d5db3c2def2e07e2`
- **SHA1:** `e0f8ca1f687630fd23c768d94190d59c0a5882cc`
- **MD5:** `c6d4d54b7115cc5a61596016507442d3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 128 B |
| Entropía | 5.05 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | ffbf38cf832db37257ed186abe30edc715cc1b6ac0490d62d5db3c2def2e07e2 | static_analysis |
| ip | 40.119.41.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
