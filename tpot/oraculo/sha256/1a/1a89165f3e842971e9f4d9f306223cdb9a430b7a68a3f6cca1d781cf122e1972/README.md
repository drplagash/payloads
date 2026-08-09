# 🧬 Payload Analysis

`1a89165f3e842971e9f4d9f306223cdb9a430b7a68a3f6cca1d781cf122e1972`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:37:42+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1a89165f3e842971e9f4d9f306223cdb9a430b7a68a3f6cca1d781cf122e1972`
- **SHA1:** `810f0f65775016c949fb54e8c548161b12fc5f37`
- **MD5:** `b4c1b8492bcd0e373a5f9df6f5aea439`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 419 B |
| Entropía | 5.38 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 190.179.166.XXX | static_analysis |
| ip | 54.177.117.XXX | static_analysis |
| hash | 1a89165f3e842971e9f4d9f306223cdb9a430b7a68a3f6cca1d781cf122e1972 | static_analysis |
| ip | 209.141.52.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
