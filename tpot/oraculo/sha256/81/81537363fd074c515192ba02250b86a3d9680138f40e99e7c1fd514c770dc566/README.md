# 🧬 Payload Analysis

`81537363fd074c515192ba02250b86a3d9680138f40e99e7c1fd514c770dc566`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:23:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `81537363fd074c515192ba02250b86a3d9680138f40e99e7c1fd514c770dc566`
- **SHA1:** `3f306688fe0e532c524d8184ac6cf3ac5f2b39a3`
- **MD5:** `b599a37bee76803d52705ed74e7617cf`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 209 B |
| Entropía | 5.34 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 136.0.0.XXX | static_analysis |
| ip | 190.179.128.XXX | static_analysis |
| hash | 81537363fd074c515192ba02250b86a3d9680138f40e99e7c1fd514c770dc566 | static_analysis |
| ip | 52.200.76.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
