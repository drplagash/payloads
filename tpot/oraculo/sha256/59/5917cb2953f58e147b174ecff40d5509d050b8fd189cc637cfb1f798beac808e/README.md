# 🧬 Payload Analysis

`5917cb2953f58e147b174ecff40d5509d050b8fd189cc637cfb1f798beac808e`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5917cb2953f58e147b174ecff40d5509d050b8fd189cc637cfb1f798beac808e`
- **SHA1:** `3758c07c6012c5734460cfc0ec4a5159c543c48f`
- **MD5:** `5c64fcaa9b8d888a701cb70890b9d6dd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 795 B |
| Entropía | 5.48 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 148.182.22.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 5917cb2953f58e147b174ecff40d5509d050b8fd189cc637cfb1f798beac808e | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
