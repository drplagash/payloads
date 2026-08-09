# 🧬 Payload Analysis

`3f93b382739e1a51437ecb8af4b31f022d2714e51c55c9c6699ea94ef2b9c51c`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3f93b382739e1a51437ecb8af4b31f022d2714e51c55c9c6699ea94ef2b9c51c`
- **SHA1:** `e6a0e91de082e10016f7a2c760c5b5ca38adc6cd`
- **MD5:** `0a93abe8a396a204260cbea5e027d2c9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 791 B |
| Entropía | 5.49 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 11.108.27.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 3f93b382739e1a51437ecb8af4b31f022d2714e51c55c9c6699ea94ef2b9c51c | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
