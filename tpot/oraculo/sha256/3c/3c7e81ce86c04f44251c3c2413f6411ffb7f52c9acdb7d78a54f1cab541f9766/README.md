# 🧬 Payload Analysis

`3c7e81ce86c04f44251c3c2413f6411ffb7f52c9acdb7d78a54f1cab541f9766`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3c7e81ce86c04f44251c3c2413f6411ffb7f52c9acdb7d78a54f1cab541f9766`
- **SHA1:** `d7d5c50bbb7a557c20214556da5d167bda5bf7e0`
- **MD5:** `e5c3c9eaa5147e40d8a987c6c4d41a7d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (403), with CRLF line terminators |
| Tamaño | 997 B |
| Entropía | 5.52 |
| Strings | 16 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (403), with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| ip | 45.153.34.XXX | static_analysis |
| hash | 3c7e81ce86c04f44251c3c2413f6411ffb7f52c9acdb7d78a54f1cab541f9766 | static_analysis |
| ip | 193.26.115.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
