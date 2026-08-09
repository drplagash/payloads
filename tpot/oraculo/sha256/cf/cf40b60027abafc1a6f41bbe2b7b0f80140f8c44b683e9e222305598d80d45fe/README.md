# 🧬 Payload Analysis

`cf40b60027abafc1a6f41bbe2b7b0f80140f8c44b683e9e222305598d80d45fe`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cf40b60027abafc1a6f41bbe2b7b0f80140f8c44b683e9e222305598d80d45fe`
- **SHA1:** `bb5589dd3426bbf52da107efbb1b69f3be6c5cf0`
- **MD5:** `30736d768296b5c8789fc05e0d1093b3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Excel 3 BIFF 3 |
| Tamaño | 4.0 KiB |
| Entropía | 7.94 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Excel 3 BIFF 3; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | cf40b60027abafc1a6f41bbe2b7b0f80140f8c44b683e9e222305598d80d45fe | static_analysis |
| ip | 45.150.206.XXX | artifact_source |

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
