# 🧬 Payload Analysis

`e5bd918088125cf8fda06ec3421a65809391fc0afdefa137ba87855646d8da92`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e5bd918088125cf8fda06ec3421a65809391fc0afdefa137ba87855646d8da92`
- **SHA1:** `f44dc9fbb8cc40c3925d8c2c005b826146ce284f`
- **MD5:** `e8365e247292cc6e192a9051cb504d5d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 124 B |
| Entropía | 5.12 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| hash | e5bd918088125cf8fda06ec3421a65809391fc0afdefa137ba87855646d8da92 | static_analysis |
| ip | 20.15.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
