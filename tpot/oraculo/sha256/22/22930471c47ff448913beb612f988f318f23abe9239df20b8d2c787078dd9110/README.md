# 🧬 Payload Analysis

`22930471c47ff448913beb612f988f318f23abe9239df20b8d2c787078dd9110`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `22930471c47ff448913beb612f988f318f23abe9239df20b8d2c787078dd9110`
- **SHA1:** `2b497d9ffd2ccf2dadee7a6d1c14ffc622aaf44a`
- **MD5:** `e8f97d46b286cdcd0367aac7d1cb0799`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 940 B |
| Entropía | 5.67 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 134.0.0.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| hash | 22930471c47ff448913beb612f988f318f23abe9239df20b8d2c787078dd9110 | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
