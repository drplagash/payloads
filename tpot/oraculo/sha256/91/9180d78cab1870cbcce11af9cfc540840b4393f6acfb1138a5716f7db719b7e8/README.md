# 🧬 Payload Analysis

`9180d78cab1870cbcce11af9cfc540840b4393f6acfb1138a5716f7db719b7e8`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:58:35+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9180d78cab1870cbcce11af9cfc540840b4393f6acfb1138a5716f7db719b7e8`
- **SHA1:** `78101a97b53f2b9eb268aec5afcf5df2543cb86a`
- **MD5:** `37ea40112a8a922bfb6a80ba93b19e3c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 435 B |
| Entropía | 7.59 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.6; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 9180d78cab1870cbcce11af9cfc540840b4393f6acfb1138a5716f7db719b7e8 | static_analysis |
| ip | 59.52.103.XXX | artifact_source |

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
