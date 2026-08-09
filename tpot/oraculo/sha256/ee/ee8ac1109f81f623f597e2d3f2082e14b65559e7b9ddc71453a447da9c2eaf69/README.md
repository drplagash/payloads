# 🧬 Payload Analysis

`ee8ac1109f81f623f597e2d3f2082e14b65559e7b9ddc71453a447da9c2eaf69`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ee8ac1109f81f623f597e2d3f2082e14b65559e7b9ddc71453a447da9c2eaf69`
- **SHA1:** `29a565d7e197c1791da0414a999e7b1f1a7ce281`
- **MD5:** `d4ead34c9c2a00b81b84ed0c92613f79`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (404), with CRLF line terminators |
| Tamaño | 955 B |
| Entropía | 5.48 |
| Strings | 16 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (404), with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| ip | 204.10.194.XXX | static_analysis |
| hash | ee8ac1109f81f623f597e2d3f2082e14b65559e7b9ddc71453a447da9c2eaf69 | static_analysis |
| ip | 124.198.131.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
