# 🧬 Payload Analysis

`67b2d620ba22655dd181d8575aeaaf44516bb5e9da3d34ad50c6df6000f2ca67`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `67b2d620ba22655dd181d8575aeaaf44516bb5e9da3d34ad50c6df6000f2ca67`
- **SHA1:** `3cd522a335cd1fc2694a9dfbcbb7222a2833e2d9`
- **MD5:** `59c95e4d9cc03281dbd8e536023e0201`

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
| ip | 185.120.174.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 67b2d620ba22655dd181d8575aeaaf44516bb5e9da3d34ad50c6df6000f2ca67 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
