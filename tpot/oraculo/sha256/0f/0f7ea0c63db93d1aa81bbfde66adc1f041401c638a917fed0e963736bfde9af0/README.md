# 🧬 Payload Analysis

`0f7ea0c63db93d1aa81bbfde66adc1f041401c638a917fed0e963736bfde9af0`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:26:17+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0f7ea0c63db93d1aa81bbfde66adc1f041401c638a917fed0e963736bfde9af0`
- **SHA1:** `1d0e05bed8c401839a3df6e8a90481400ae7bfc5`
- **MD5:** `41236ea78f9264e657474cee3b48e31c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0xb8864908 3bf32c50 |
| Tamaño | 4.0 KiB |
| Entropía | 7.94 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0xb8864908 3bf32c50; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 0f7ea0c63db93d1aa81bbfde66adc1f041401c638a917fed0e963736bfde9af0 | static_analysis |
| ip | 189.79.136.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | archive container |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
