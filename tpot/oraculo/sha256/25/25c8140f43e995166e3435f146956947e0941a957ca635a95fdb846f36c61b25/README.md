# 🧬 Payload Analysis

`25c8140f43e995166e3435f146956947e0941a957ca635a95fdb846f36c61b25`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `25c8140f43e995166e3435f146956947e0941a957ca635a95fdb846f36c61b25`
- **SHA1:** `5b5605e7344dfb84308245831b99c8f45b1cceaf`
- **MD5:** `35378aee404e4dbc90d4dbae5ccc5824`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.48 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 120.82.226.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 25c8140f43e995166e3435f146956947e0941a957ca635a95fdb846f36c61b25 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
