# 🧬 Payload Analysis

`ad20ee45bbecf05c357034d7849ff39e46b0672903ba3e6a1f9bbc6ee0f8d3e3`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:40+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ad20ee45bbecf05c357034d7849ff39e46b0672903ba3e6a1f9bbc6ee0f8d3e3`
- **SHA1:** `0b013308fe2f92afba792227dd30a8dcc57473aa`
- **MD5:** `41f77ab945c77a30c7801fce8dcb0134`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 549 B |
| Entropía | 5.39 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| hash | ad20ee45bbecf05c357034d7849ff39e46b0672903ba3e6a1f9bbc6ee0f8d3e3 | static_analysis |
| ip | 141.98.11.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
