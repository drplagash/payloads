# 🧬 Payload Analysis

`db209716aff42d35911e35f7f52256474a66dfc39fe8706baf61ea6549d28bef`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:52+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `db209716aff42d35911e35f7f52256474a66dfc39fe8706baf61ea6549d28bef`
- **SHA1:** `b0d2eeb35c9695794f732f0174b51bb0afc25b95`
- **MD5:** `ac7a86dd5e2db40faf125f0f52eaee8f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 50 B |
| Entropía | 4.29 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | db209716aff42d35911e35f7f52256474a66dfc39fe8706baf61ea6549d28bef | static_analysis |
| ip | 195.178.110.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
