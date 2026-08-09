# 🧬 Payload Analysis

`9bee4eecb5d968d51dfaf3eab2527a43f65530dfecf45366b7693dd0b927c660`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:55:35+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9bee4eecb5d968d51dfaf3eab2527a43f65530dfecf45366b7693dd0b927c660`
- **SHA1:** `3f4ad074d15da1d0414ddc100e11fd9876109bc5`
- **MD5:** `5d938e96a442693d9d3197c002a6f175`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 115 B |
| Entropía | 5.07 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| hash | 9bee4eecb5d968d51dfaf3eab2527a43f65530dfecf45366b7693dd0b927c660 | static_analysis |
| ip | 176.65.149.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
