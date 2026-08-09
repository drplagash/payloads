# 🧬 Payload Analysis

`cf94c00ecaff9e49bd4dd108401f7f8c48b8b42aed1993e81755c98b0efc3016`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cf94c00ecaff9e49bd4dd108401f7f8c48b8b42aed1993e81755c98b0efc3016`
- **SHA1:** `04a7eb6e20279040015941f49589ce0f6be4511d`
- **MD5:** `6c05440d7eae4d43361c313dc26bc0a7`

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
| ip | 152.118.145.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | cf94c00ecaff9e49bd4dd108401f7f8c48b8b42aed1993e81755c98b0efc3016 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
