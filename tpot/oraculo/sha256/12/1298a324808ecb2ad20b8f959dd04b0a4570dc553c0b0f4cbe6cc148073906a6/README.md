# 🧬 Payload Analysis

`1298a324808ecb2ad20b8f959dd04b0a4570dc553c0b0f4cbe6cc148073906a6`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:36:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1298a324808ecb2ad20b8f959dd04b0a4570dc553c0b0f4cbe6cc148073906a6`
- **MD5:** `ecb5ebbaacacd46c5ede6f9ef5d106f8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 416 B |
| Entropía | 5.38 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 162.217.103.XXX | static_analysis |
| ip | 190.179.174.XXX | static_analysis |
| hash | 1298a324808ecb2ad20b8f959dd04b0a4570dc553c0b0f4cbe6cc148073906a6 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
