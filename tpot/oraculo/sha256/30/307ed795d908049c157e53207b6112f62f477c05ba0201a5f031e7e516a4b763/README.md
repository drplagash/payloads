# 🧬 Payload Analysis

`307ed795d908049c157e53207b6112f62f477c05ba0201a5f031e7e516a4b763`

## 📌 Resumen

La evidencia técnica es compatible con **Suspicious Payload**. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `307ed795d908049c157e53207b6112f62f477c05ba0201a5f031e7e516a4b763`
- **SHA1:** `b861a3cdd4f86c8ac3f1ff817709ff82961f8c81`
- **MD5:** `7e7359af4941cca79e96a1a11afd4042`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Solitaire Image Recorder format |
| Tamaño | 1.4 KiB |
| Entropía | 7.88 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Solitaire Image Recorder format; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 307ed795d908049c157e53207b6112f62f477c05ba0201a5f031e7e516a4b763 | static_analysis |
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
