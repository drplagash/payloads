# 🧬 Payload Analysis

`f0b639bd1e75d9d31f8b3d71695a8fffe58f649cf9f403bacde7cfbdaab8c417`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f0b639bd1e75d9d31f8b3d71695a8fffe58f649cf9f403bacde7cfbdaab8c417`
- **SHA1:** `46284a37c627c80ca585dc551e55fc0cbf63ef7e`
- **MD5:** `cb45d31f9d2b2ee378a206ed448973df`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 789 B |
| Entropía | 5.51 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 156.57.31.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | f0b639bd1e75d9d31f8b3d71695a8fffe58f649cf9f403bacde7cfbdaab8c417 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
