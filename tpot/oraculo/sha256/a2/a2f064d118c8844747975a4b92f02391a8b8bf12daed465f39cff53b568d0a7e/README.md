# 🧬 Payload Analysis

`a2f064d118c8844747975a4b92f02391a8b8bf12daed465f39cff53b568d0a7e`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:55+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a2f064d118c8844747975a4b92f02391a8b8bf12daed465f39cff53b568d0a7e`
- **SHA1:** `ec53b1f3ceb8fa7041a5713e4934966b83975efd`
- **MD5:** `6b0827bbd159fd4a325adb682777df9b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (404), with CRLF line terminators |
| Tamaño | 955 B |
| Entropía | 5.48 |
| Strings | 16 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (404), with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| ip | 204.10.194.XXX | static_analysis |
| hash | a2f064d118c8844747975a4b92f02391a8b8bf12daed465f39cff53b568d0a7e | static_analysis |
| ip | 124.198.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
