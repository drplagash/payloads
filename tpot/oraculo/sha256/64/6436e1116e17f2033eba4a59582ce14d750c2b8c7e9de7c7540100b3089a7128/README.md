# 🧬 Payload Analysis

`6436e1116e17f2033eba4a59582ce14d750c2b8c7e9de7c7540100b3089a7128`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:00:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6436e1116e17f2033eba4a59582ce14d750c2b8c7e9de7c7540100b3089a7128`
- **SHA1:** `3c512e7320d56df480163f33a91c89e2665be5ff`
- **MD5:** `2ccbb1acaa0104869243c48eb3ee12ad`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Unicode text, UTF-8 text, with CRLF line terminators |
| Tamaño | 1.1 KiB |
| Entropía | 5.58 |
| Strings | 35 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Unicode text, UTF-8 text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 160.119.71.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 6436e1116e17f2033eba4a59582ce14d750c2b8c7e9de7c7540100b3089a7128 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
