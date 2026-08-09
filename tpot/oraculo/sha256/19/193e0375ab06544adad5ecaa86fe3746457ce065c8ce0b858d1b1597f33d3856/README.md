# 🧬 Payload Analysis

`193e0375ab06544adad5ecaa86fe3746457ce065c8ce0b858d1b1597f33d3856`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:31:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `193e0375ab06544adad5ecaa86fe3746457ce065c8ce0b858d1b1597f33d3856`
- **SHA1:** `55abdb42abd4249f0e6830289d460c0862f09122`
- **MD5:** `914da2a9fdd9d1caa197c3a2f94716e6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 738 B |
| Entropía | 5.36 |
| Strings | 22 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | 193e0375ab06544adad5ecaa86fe3746457ce065c8ce0b858d1b1597f33d3856 | static_analysis |
| ip | 217.160.24.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
