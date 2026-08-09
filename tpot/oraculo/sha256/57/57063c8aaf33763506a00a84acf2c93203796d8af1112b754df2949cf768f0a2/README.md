# 🧬 Payload Analysis

`57063c8aaf33763506a00a84acf2c93203796d8af1112b754df2949cf768f0a2`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:49:32+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `57063c8aaf33763506a00a84acf2c93203796d8af1112b754df2949cf768f0a2`
- **SHA1:** `98a6096aba3c48f3dc4ee836e93c31b598bb8a22`
- **MD5:** `770e6849562bec3faafa13f5f4307200`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Dyalog APL version 48.-33 |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Dyalog APL version 48.-33; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 57063c8aaf33763506a00a84acf2c93203796d8af1112b754df2949cf768f0a2 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | candidate malware unknown |
| Prioridad | medium |
| Score | 5.0 |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
