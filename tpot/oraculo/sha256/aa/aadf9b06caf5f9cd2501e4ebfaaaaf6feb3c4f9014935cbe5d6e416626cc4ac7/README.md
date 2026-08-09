# 🧬 Payload Analysis

`aadf9b06caf5f9cd2501e4ebfaaaaf6feb3c4f9014935cbe5d6e416626cc4ac7`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:01:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `aadf9b06caf5f9cd2501e4ebfaaaaf6feb3c4f9014935cbe5d6e416626cc4ac7`
- **SHA1:** `2b1d5fc4ffae8be510d2e6416914acc3bfc17133`
- **MD5:** `139e85fc52774fe041cb579133114dcb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 103 B |
| Entropía | 5.11 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | aadf9b06caf5f9cd2501e4ebfaaaaf6feb3c4f9014935cbe5d6e416626cc4ac7 | static_analysis |
| ip | 31.59.160.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
