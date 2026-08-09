# 🧬 Payload Analysis

`d4e858353e52a24677ff3c129787ccdf844bb3e77a6b79285f166c84be368e74`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d4e858353e52a24677ff3c129787ccdf844bb3e77a6b79285f166c84be368e74`
- **SHA1:** `db4d234800b9d9deba52b281129d71af9515aa1b`
- **MD5:** `4373a5c2b50e0c6ff70d16c83e43cfc5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 522 B |
| Entropía | 5.4 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | d4e858353e52a24677ff3c129787ccdf844bb3e77a6b79285f166c84be368e74 | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
