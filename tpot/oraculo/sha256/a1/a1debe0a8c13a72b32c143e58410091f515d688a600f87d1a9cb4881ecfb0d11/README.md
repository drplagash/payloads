# 🧬 Payload Analysis

`a1debe0a8c13a72b32c143e58410091f515d688a600f87d1a9cb4881ecfb0d11`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:10:14+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a1debe0a8c13a72b32c143e58410091f515d688a600f87d1a9cb4881ecfb0d11`
- **SHA1:** `0c63cfaec22111fc8abf97add1e03059bd474002`
- **MD5:** `878bf9775d5555d1a51afc7d8ab8a9db`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (377), with CRLF line terminators |
| Tamaño | 1.1 KiB |
| Entropía | 5.62 |
| Strings | 20 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (377), with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 120.0.0.XXX | static_analysis |
| ip | 190.179.172.XXX | static_analysis |
| hash | a1debe0a8c13a72b32c143e58410091f515d688a600f87d1a9cb4881ecfb0d11 | static_analysis |
| ip | 198.50.239.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
