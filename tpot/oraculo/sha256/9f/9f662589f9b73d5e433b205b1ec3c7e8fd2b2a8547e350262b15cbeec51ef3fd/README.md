# 🧬 Payload Analysis

`9f662589f9b73d5e433b205b1ec3c7e8fd2b2a8547e350262b15cbeec51ef3fd`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9f662589f9b73d5e433b205b1ec3c7e8fd2b2a8547e350262b15cbeec51ef3fd`
- **SHA1:** `d9c76ef977a18b182c9acf0f39a03e048e797be8`
- **MD5:** `746881fec39c4ab065a4653387931122`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 803 B |
| Entropía | 5.52 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 152.164.174.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 9f662589f9b73d5e433b205b1ec3c7e8fd2b2a8547e350262b15cbeec51ef3fd | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
