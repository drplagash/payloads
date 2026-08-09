# 🧬 Payload Analysis

`07c56550a831352a4c02f0bb0ac6e61c61009f56cfb49e312f65263eeb6464be`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `07c56550a831352a4c02f0bb0ac6e61c61009f56cfb49e312f65263eeb6464be`
- **SHA1:** `c7c1b4772a340dac66fb5f5e4e497a1cdc4b5be7`
- **MD5:** `5b7f725665f0d995ec8a1fb4d3348425`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 795 B |
| Entropía | 5.53 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 164.58.153.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 07c56550a831352a4c02f0bb0ac6e61c61009f56cfb49e312f65263eeb6464be | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
