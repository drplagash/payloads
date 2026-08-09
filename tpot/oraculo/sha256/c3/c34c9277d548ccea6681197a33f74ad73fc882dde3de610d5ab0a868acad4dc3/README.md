# 🧬 Payload Analysis

`c34c9277d548ccea6681197a33f74ad73fc882dde3de610d5ab0a868acad4dc3`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:02:12+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c34c9277d548ccea6681197a33f74ad73fc882dde3de610d5ab0a868acad4dc3`
- **SHA1:** `d67363bf5daf5889b273e5637773947dd9c19b8f`
- **MD5:** `fcb0b71f100c9d0412fc60b3e4659f4a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Dyalog APL version 10.-82 |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Dyalog APL version 10.-82; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | c34c9277d548ccea6681197a33f74ad73fc882dde3de610d5ab0a868acad4dc3 | static_analysis |
| ip | 37.57.94.XXX | artifact_source |

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
