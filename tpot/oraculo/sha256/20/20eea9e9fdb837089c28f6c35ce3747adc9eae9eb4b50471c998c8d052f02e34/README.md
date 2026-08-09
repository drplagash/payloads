# 🧬 Payload Analysis

`20eea9e9fdb837089c28f6c35ce3747adc9eae9eb4b50471c998c8d052f02e34`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `20eea9e9fdb837089c28f6c35ce3747adc9eae9eb4b50471c998c8d052f02e34`
- **SHA1:** `587ef8ec3da404e821e055b620ee97f593cc0aed`
- **MD5:** `003da673e2034346a312cd25b89e1309`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 801 B |
| Entropía | 5.49 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 177.42.219.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 20eea9e9fdb837089c28f6c35ce3747adc9eae9eb4b50471c998c8d052f02e34 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
