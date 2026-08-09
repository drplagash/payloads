# 🧬 Payload Analysis

`50db4db9f9a8f6ee76d908f7345616067e9b0ea20a4b95321a5de626991f94c0`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `50db4db9f9a8f6ee76d908f7345616067e9b0ea20a4b95321a5de626991f94c0`
- **SHA1:** `f07be99e27c27fc237a759179b892b4c47ee60c8`
- **MD5:** `f1ac87f67cb4941e4475faa2021381de`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.51 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 149.94.130.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 50db4db9f9a8f6ee76d908f7345616067e9b0ea20a4b95321a5de626991f94c0 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
