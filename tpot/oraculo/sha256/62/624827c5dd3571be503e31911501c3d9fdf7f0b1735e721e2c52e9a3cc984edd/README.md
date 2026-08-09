# 🧬 Payload Analysis

`624827c5dd3571be503e31911501c3d9fdf7f0b1735e721e2c52e9a3cc984edd`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:17:49+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `624827c5dd3571be503e31911501c3d9fdf7f0b1735e721e2c52e9a3cc984edd`
- **SHA1:** `5862ae9a78bc3bd161ef5e3377e58c9addad6865`
- **MD5:** `5f58db49cbcd5bb99a8535ede4672f1d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 312 B |
| Entropía | 5.24 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| hash | 624827c5dd3571be503e31911501c3d9fdf7f0b1735e721e2c52e9a3cc984edd | static_analysis |
| ip | 47.254.135.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
