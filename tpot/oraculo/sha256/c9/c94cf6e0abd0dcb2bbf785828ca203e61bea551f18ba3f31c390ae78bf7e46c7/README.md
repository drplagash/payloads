# 🧬 Payload Analysis

`c94cf6e0abd0dcb2bbf785828ca203e61bea551f18ba3f31c390ae78bf7e46c7`

## 📌 Resumen

La evidencia técnica es compatible con **Suspicious Payload**. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:27:36.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c94cf6e0abd0dcb2bbf785828ca203e61bea551f18ba3f31c390ae78bf7e46c7`
- **SHA1:** `3b323380d7d0540d372ebef9a3602687fd2d80e3`
- **MD5:** `04c0015e6cec83a4110bf731d63631a8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Dyalog APL version 112.21 |
| Tamaño | 1.4 KiB |
| Entropía | 7.87 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Dyalog APL version 112.21; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | c94cf6e0abd0dcb2bbf785828ca203e61bea551f18ba3f31c390ae78bf7e46c7 | static_analysis |
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
