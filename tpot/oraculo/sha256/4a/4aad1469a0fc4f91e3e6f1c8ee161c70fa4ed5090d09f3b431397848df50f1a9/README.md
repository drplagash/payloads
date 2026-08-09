# 🧬 Payload Analysis

`4aad1469a0fc4f91e3e6f1c8ee161c70fa4ed5090d09f3b431397848df50f1a9`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4aad1469a0fc4f91e3e6f1c8ee161c70fa4ed5090d09f3b431397848df50f1a9`
- **SHA1:** `e9af6c4b5253a3593ee77c44fcae66e99353fee5`
- **MD5:** `c3ee748545a16fcbc498c43d96286025`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 692 B |
| Entropía | 5.4 |
| Strings | 21 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | 4aad1469a0fc4f91e3e6f1c8ee161c70fa4ed5090d09f3b431397848df50f1a9 | static_analysis |
| ip | 89.190.156.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
