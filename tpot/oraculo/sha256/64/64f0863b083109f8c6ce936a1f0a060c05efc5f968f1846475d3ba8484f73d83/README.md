# 🧬 Payload Analysis

`64f0863b083109f8c6ce936a1f0a060c05efc5f968f1846475d3ba8484f73d83`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:57:27+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `64f0863b083109f8c6ce936a1f0a060c05efc5f968f1846475d3ba8484f73d83`
- **SHA1:** `ce28538103bd8e98e11344bf59d8eae65fdaacfc`
- **MD5:** `027cb46b48aa4ae36fbbe0e13d324124`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Linux jffs2 filesystem data big endian |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Linux jffs2 filesystem data big endian; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 64f0863b083109f8c6ce936a1f0a060c05efc5f968f1846475d3ba8484f73d83 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
