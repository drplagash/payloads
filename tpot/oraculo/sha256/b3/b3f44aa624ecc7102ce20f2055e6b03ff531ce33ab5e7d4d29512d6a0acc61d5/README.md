# 🧬 Payload Analysis

`b3f44aa624ecc7102ce20f2055e6b03ff531ce33ab5e7d4d29512d6a0acc61d5`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:23:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b3f44aa624ecc7102ce20f2055e6b03ff531ce33ab5e7d4d29512d6a0acc61d5`
- **SHA1:** `a73290b601c4e185512fdd562537eb13cb43f395`
- **MD5:** `bd2d1dff8bbd701e8d742db2698b1096`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 210 B |
| Entropía | 5.36 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 136.0.0.XXX | static_analysis |
| ip | 190.179.128.XXX | static_analysis |
| hash | b3f44aa624ecc7102ce20f2055e6b03ff531ce33ab5e7d4d29512d6a0acc61d5 | static_analysis |
| ip | 52.200.76.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
