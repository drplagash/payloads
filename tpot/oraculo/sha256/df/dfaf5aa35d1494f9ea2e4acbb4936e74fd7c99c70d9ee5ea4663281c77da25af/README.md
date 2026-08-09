# 🧬 Payload Analysis

`dfaf5aa35d1494f9ea2e4acbb4936e74fd7c99c70d9ee5ea4663281c77da25af`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:17:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dfaf5aa35d1494f9ea2e4acbb4936e74fd7c99c70d9ee5ea4663281c77da25af`
- **SHA1:** `7d2cd867c14e220f2fbe1992acd6f68de0a12fa9`
- **MD5:** `9412be3a6fccb25e664f0cea0ca69bc5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 72 B |
| Entropía | 4.85 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | dfaf5aa35d1494f9ea2e4acbb4936e74fd7c99c70d9ee5ea4663281c77da25af | static_analysis |
| ip | 91.92.40.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
