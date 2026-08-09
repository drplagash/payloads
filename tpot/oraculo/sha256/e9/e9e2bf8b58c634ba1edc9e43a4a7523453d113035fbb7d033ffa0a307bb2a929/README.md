# 🧬 Payload Analysis

`e9e2bf8b58c634ba1edc9e43a4a7523453d113035fbb7d033ffa0a307bb2a929`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:51:39+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e9e2bf8b58c634ba1edc9e43a4a7523453d113035fbb7d033ffa0a307bb2a929`
- **SHA1:** `3f10a1d8f8f231eec86de62f5dd1e03abbf714d6`
- **MD5:** `94855d6be97129a28b597aaeca1fdbe3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | very old (C/A/T) troff output data |
| MIME | very old (C/A/T) troff output data |
| Tamaño | 1.4 KiB |
| Entropía | 7.88 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=very old (C/A/T) troff output data; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | e9e2bf8b58c634ba1edc9e43a4a7523453d113035fbb7d033ffa0a307bb2a929 | static_analysis |
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
