# 🧬 Payload Analysis

`1a64778d16036fc1f20728bae2e17ac04c63fa716f6fcfdc1f130d5cf9af50e5`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Ssh related.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:10:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1a64778d16036fc1f20728bae2e17ac04c63fa716f6fcfdc1f130d5cf9af50e5`
- **SHA1:** `74605b4a6940d5bb4a54dccc6342bede24b80339`
- **MD5:** `1243de8aa8edd97b31ad363c16e4e072`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 43 B |
| Entropía | 4.25 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Ssh related**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 1a64778d16036fc1f20728bae2e17ac04c63fa716f6fcfdc1f130d5cf9af50e5 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
