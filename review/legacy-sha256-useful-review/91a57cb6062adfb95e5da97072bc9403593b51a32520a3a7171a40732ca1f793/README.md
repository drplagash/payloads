# 🧬 Payload Analysis

`91a57cb6062adfb95e5da97072bc9403593b51a32520a3a7171a40732ca1f793`

## 📌 Resumen

La evidencia técnica es compatible con **Suspicious Payload**. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:44:37.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `91a57cb6062adfb95e5da97072bc9403593b51a32520a3a7171a40732ca1f793`
- **SHA1:** `cfe6fa1095ffda4bc53cd8dc98d2343b971f1bee`
- **MD5:** `c038bee7ab8f832fc83b47fd4d6a39d9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Dyalog APL DFS component file 64-bit level 1 journaled checksummed version 18.87 |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Dyalog APL DFS component file 64-bit level 1 journaled checksummed version 18.87; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 91a57cb6062adfb95e5da97072bc9403593b51a32520a3a7171a40732ca1f793 | static_analysis |
| ip | 193.201.88.XXX | artifact_source |

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
