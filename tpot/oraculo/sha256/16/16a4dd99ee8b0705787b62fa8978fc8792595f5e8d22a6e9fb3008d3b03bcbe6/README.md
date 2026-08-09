# 🧬 Payload Analysis

`16a4dd99ee8b0705787b62fa8978fc8792595f5e8d22a6e9fb3008d3b03bcbe6`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `16a4dd99ee8b0705787b62fa8978fc8792595f5e8d22a6e9fb3008d3b03bcbe6`
- **SHA1:** `63cf3b1841a7eacb73252c804afbe916c590c469`
- **MD5:** `5a80516af929840eef7b6314ca330325`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 936 B |
| Entropía | 5.62 |
| Strings | 27 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 160.119.76.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| hash | 16a4dd99ee8b0705787b62fa8978fc8792595f5e8d22a6e9fb3008d3b03bcbe6 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
