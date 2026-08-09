# 🧬 Payload Analysis

`cd3bb3357f5138eb1a3ab4afea61c9b8138828c96efa593b8891b34d28a7a942`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:10+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cd3bb3357f5138eb1a3ab4afea61c9b8138828c96efa593b8891b34d28a7a942`
- **SHA1:** `3ab5e38d8da9c999129fd4ce9fee0be8608f9d21`
- **MD5:** `3227fb06307157900ba5febb0a979f56`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 511 B |
| Entropía | 5.69 |
| Strings | 13 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | cd3bb3357f5138eb1a3ab4afea61c9b8138828c96efa593b8891b34d28a7a942 | static_analysis |
| ip | 107.189.24.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
