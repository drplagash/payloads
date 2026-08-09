# 🧬 Payload Analysis

`8895d67150fa674b29140fed0ab4fbc604ea7e1f1af700907d3208798372e037`

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

- **SHA256:** `8895d67150fa674b29140fed0ab4fbc604ea7e1f1af700907d3208798372e037`
- **SHA1:** `9e2ab9279ab073ebca832bf1bae7fb2a80464c2c`
- **MD5:** `70e04d94592ec73b62eb594d51424bcd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 320 B |
| Entropía | 7.37 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.4; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 8895d67150fa674b29140fed0ab4fbc604ea7e1f1af700907d3208798372e037 | static_analysis |
| ip | 2.57.121.XXX | artifact_source |

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
