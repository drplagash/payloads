# 🧬 Payload Analysis

`0d7e2ce3f8988ca282bdd3888142da2521f8d0a2c6c1393cc418b32c3a841ec3`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0d7e2ce3f8988ca282bdd3888142da2521f8d0a2c6c1393cc418b32c3a841ec3`
- **SHA1:** `dfe5ae4d3662bbae54cab25e4b5f5824c7a50678`
- **MD5:** `a64826136610a1a38066b61afa6a11a0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 795 B |
| Entropía | 5.51 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 194.99.234.XXX | static_analysis |
| hash | 0d7e2ce3f8988ca282bdd3888142da2521f8d0a2c6c1393cc418b32c3a841ec3 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
