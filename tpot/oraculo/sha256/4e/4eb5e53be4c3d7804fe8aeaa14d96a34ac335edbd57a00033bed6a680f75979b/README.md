# 🧬 Payload Analysis

`4eb5e53be4c3d7804fe8aeaa14d96a34ac335edbd57a00033bed6a680f75979b`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4eb5e53be4c3d7804fe8aeaa14d96a34ac335edbd57a00033bed6a680f75979b`
- **SHA1:** `87e08449a5f96281f8fa317aaabd32b31b8d2728`
- **MD5:** `36e0d9e7138d7072185aecb9eaac35ce`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 517 B |
| Entropía | 5.42 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 4eb5e53be4c3d7804fe8aeaa14d96a34ac335edbd57a00033bed6a680f75979b | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
