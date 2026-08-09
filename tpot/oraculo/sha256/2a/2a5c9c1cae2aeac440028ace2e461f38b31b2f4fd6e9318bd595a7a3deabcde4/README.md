# 🧬 Payload Analysis

`2a5c9c1cae2aeac440028ace2e461f38b31b2f4fd6e9318bd595a7a3deabcde4`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:39:05+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2a5c9c1cae2aeac440028ace2e461f38b31b2f4fd6e9318bd595a7a3deabcde4`
- **SHA1:** `ad8f4cc80ced8ef750f19b937cd8bc93c960b001`
- **MD5:** `1f4a6e149a6d68e4450b23019b4c4607`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (404), with CRLF line terminators |
| Tamaño | 956 B |
| Entropía | 5.48 |
| Strings | 16 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (404), with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.166.XXX | static_analysis |
| ip | 204.10.194.XXX | static_analysis |
| hash | 2a5c9c1cae2aeac440028ace2e461f38b31b2f4fd6e9318bd595a7a3deabcde4 | static_analysis |
| ip | 124.198.131.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
