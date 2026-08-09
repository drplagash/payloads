# 🧬 Payload Analysis

`8a244126430c6c8c84535b249190fa9035fda4d5c7329c5e9a788bdc71701e78`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8a244126430c6c8c84535b249190fa9035fda4d5c7329c5e9a788bdc71701e78`
- **SHA1:** `de0207c4db67d3ce7567a57209532afec6facc7e`
- **MD5:** `0aba46f7bae6fc6eb9ff46c606c12b51`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 549 B |
| Entropía | 5.38 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.139.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| hash | 8a244126430c6c8c84535b249190fa9035fda4d5c7329c5e9a788bdc71701e78 | static_analysis |
| ip | 141.98.11.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
