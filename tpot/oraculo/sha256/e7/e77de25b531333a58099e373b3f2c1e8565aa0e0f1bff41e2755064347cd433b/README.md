# 🧬 Payload Analysis

`e77de25b531333a58099e373b3f2c1e8565aa0e0f1bff41e2755064347cd433b`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:46:43+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e77de25b531333a58099e373b3f2c1e8565aa0e0f1bff41e2755064347cd433b`
- **SHA1:** `63a5874a67f0e96f8c13546b06ee25530f43f2b6`
- **MD5:** `f204e7cb9019d6765bfb521ef479c7f0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 128 B |
| Entropía | 5.11 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.163.XXX | static_analysis |
| hash | e77de25b531333a58099e373b3f2c1e8565aa0e0f1bff41e2755064347cd433b | static_analysis |
| ip | 47.96.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
