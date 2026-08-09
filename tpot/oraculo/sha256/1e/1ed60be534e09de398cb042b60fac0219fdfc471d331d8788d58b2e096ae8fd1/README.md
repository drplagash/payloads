# 🧬 Payload Analysis

`1ed60be534e09de398cb042b60fac0219fdfc471d331d8788d58b2e096ae8fd1`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1ed60be534e09de398cb042b60fac0219fdfc471d331d8788d58b2e096ae8fd1`
- **SHA1:** `86a46734cb6e4dd53d18ee9fb9f17ba49c5c5363`
- **MD5:** `bd914abf8ac975e9dfbeec910c3f5f21`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 791 B |
| Entropía | 5.54 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 15.97.64.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 1ed60be534e09de398cb042b60fac0219fdfc471d331d8788d58b2e096ae8fd1 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
