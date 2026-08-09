# 🧬 Payload Analysis

`6c134ccc81d1e9bdb347d5034e586dcbcc091063a6b0dd8843195a9d3a3428ff`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:27:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6c134ccc81d1e9bdb347d5034e586dcbcc091063a6b0dd8843195a9d3a3428ff`
- **SHA1:** `eabd795b6f9ac69f35ab6ff1dc9c7259f2fa8d7b`
- **MD5:** `a542a4aa87088fe22f913e0796a047a2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 103 B |
| Entropía | 5.09 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| hash | 6c134ccc81d1e9bdb347d5034e586dcbcc091063a6b0dd8843195a9d3a3428ff | static_analysis |
| ip | 93.123.72.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
