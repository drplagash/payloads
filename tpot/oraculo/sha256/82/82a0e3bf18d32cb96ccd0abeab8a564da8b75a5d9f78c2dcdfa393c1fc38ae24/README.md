# 🧬 Payload Analysis

`82a0e3bf18d32cb96ccd0abeab8a564da8b75a5d9f78c2dcdfa393c1fc38ae24`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:49:32+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `82a0e3bf18d32cb96ccd0abeab8a564da8b75a5d9f78c2dcdfa393c1fc38ae24`
- **SHA1:** `3a816decf84c7cbe1612d2f8495611a36f22cc16`
- **MD5:** `ba3b9fa1f632ae0cfb0070b897a1b110`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 522 B |
| Entropía | 5.43 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 82a0e3bf18d32cb96ccd0abeab8a564da8b75a5d9f78c2dcdfa393c1fc38ae24 | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
