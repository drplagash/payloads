# 🧬 Payload Analysis

`793465fd0697d72d084f7e0dcf5d9727934f526dac995f4dffa40b7ef2f90d94`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `793465fd0697d72d084f7e0dcf5d9727934f526dac995f4dffa40b7ef2f90d94`
- **SHA1:** `e9fd8556452a9e8158213eca9205b34fb981eb81`
- **MD5:** `4469bac52469d966839c50ab839870af`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF, LF line terminators |
| Tamaño | 239 B |
| Entropía | 5.43 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF, LF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 141.98.9.XXX | static_analysis |
| hash | 793465fd0697d72d084f7e0dcf5d9727934f526dac995f4dffa40b7ef2f90d94 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
