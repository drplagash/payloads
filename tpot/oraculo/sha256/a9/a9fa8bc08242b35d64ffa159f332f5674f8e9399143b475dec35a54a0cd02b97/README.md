# 🧬 Payload Analysis

`a9fa8bc08242b35d64ffa159f332f5674f8e9399143b475dec35a54a0cd02b97`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a9fa8bc08242b35d64ffa159f332f5674f8e9399143b475dec35a54a0cd02b97`
- **SHA1:** `ae86016327094e76a75b7521c94f784ebfe59d91`
- **MD5:** `ca8bd976c1a36901bf101b354e4c1071`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 801 B |
| Entropía | 5.52 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 145.206.48.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | a9fa8bc08242b35d64ffa159f332f5674f8e9399143b475dec35a54a0cd02b97 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
