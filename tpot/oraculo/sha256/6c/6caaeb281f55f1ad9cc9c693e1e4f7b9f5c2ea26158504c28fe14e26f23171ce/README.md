# 🧬 Payload Analysis

`6caaeb281f55f1ad9cc9c693e1e4f7b9f5c2ea26158504c28fe14e26f23171ce`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:23:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6caaeb281f55f1ad9cc9c693e1e4f7b9f5c2ea26158504c28fe14e26f23171ce`
- **SHA1:** `b7b9f2e815c85f4beba8c32820674c79c55f73c7`
- **MD5:** `02ccd02c18a870dc4954c9f98ec81371`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 117 B |
| Entropía | 4.88 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| hash | 6caaeb281f55f1ad9cc9c693e1e4f7b9f5c2ea26158504c28fe14e26f23171ce | static_analysis |
| ip | 165.22.76.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
