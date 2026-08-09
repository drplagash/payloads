# 🧬 Payload Analysis

`5bc3c9d5f4e1866d30160395888806fbaf0e482f224963e6693bca91af48c939`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:07:44+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5bc3c9d5f4e1866d30160395888806fbaf0e482f224963e6693bca91af48c939`
- **SHA1:** `41e0f520b907f1c4cc6132eac9d4ef3d608b2779`
- **MD5:** `168d9195f8bec4e2d545e3cd17a049e5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 129 B |
| Entropía | 5.13 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.172.XXX | static_analysis |
| hash | 5bc3c9d5f4e1866d30160395888806fbaf0e482f224963e6693bca91af48c939 | static_analysis |
| ip | 135.237.123.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
