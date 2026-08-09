# 🧬 Payload Analysis

`b7b95289e4c7ca2ed4afb32a56846f1d35a920e16c6e4dc2a7b53e5bc77b996a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b7b95289e4c7ca2ed4afb32a56846f1d35a920e16c6e4dc2a7b53e5bc77b996a`
- **SHA1:** `3afcd7d8d3cc1c945c84dbd01ae86889b0186154`
- **MD5:** `5f5598922baa448f6e17f4a911a6c017`

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
| ip | 178.125.39.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | b7b95289e4c7ca2ed4afb32a56846f1d35a920e16c6e4dc2a7b53e5bc77b996a | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
