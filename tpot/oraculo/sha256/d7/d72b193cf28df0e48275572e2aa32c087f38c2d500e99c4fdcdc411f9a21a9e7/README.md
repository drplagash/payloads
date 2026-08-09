# 🧬 Payload Analysis

`d72b193cf28df0e48275572e2aa32c087f38c2d500e99c4fdcdc411f9a21a9e7`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:19+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d72b193cf28df0e48275572e2aa32c087f38c2d500e99c4fdcdc411f9a21a9e7`
- **SHA1:** `59b46f90616f3d30b02b1dec4935e5654a591b96`
- **MD5:** `6e38157ddd44ee6fa3b5deeac937d066`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 801 B |
| Entropía | 5.49 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 116.124.144.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | d72b193cf28df0e48275572e2aa32c087f38c2d500e99c4fdcdc411f9a21a9e7 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
