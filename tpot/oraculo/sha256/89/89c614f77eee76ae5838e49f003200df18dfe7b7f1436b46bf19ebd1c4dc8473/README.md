# 🧬 Payload Analysis

`89c614f77eee76ae5838e49f003200df18dfe7b7f1436b46bf19ebd1c4dc8473`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:07+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `89c614f77eee76ae5838e49f003200df18dfe7b7f1436b46bf19ebd1c4dc8473`
- **SHA1:** `5c5eb2a40e9f4a9ba1ff2a8beab963f46477d973`
- **MD5:** `1efd17ec5371e84d774489aa6e763c23`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 445 B |
| Entropía | 5.56 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.160.XXX | static_analysis |
| hash | 89c614f77eee76ae5838e49f003200df18dfe7b7f1436b46bf19ebd1c4dc8473 | static_analysis |
| ip | 91.224.92.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
