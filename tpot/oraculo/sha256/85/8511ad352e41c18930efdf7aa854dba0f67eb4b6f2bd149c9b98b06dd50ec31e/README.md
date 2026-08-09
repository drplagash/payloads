# 🧬 Payload Analysis

`8511ad352e41c18930efdf7aa854dba0f67eb4b6f2bd149c9b98b06dd50ec31e`

## 📌 Resumen

Artefacto clasificado como **Suspicious Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:03:26+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8511ad352e41c18930efdf7aa854dba0f67eb4b6f2bd149c9b98b06dd50ec31e`
- **SHA1:** `b86e74365143de1381de227b663e5c700351d8f1`
- **MD5:** `39670339377aabb24cdc3d0ce5eba99f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Public Key |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Public Key; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 8511ad352e41c18930efdf7aa854dba0f67eb4b6f2bd149c9b98b06dd50ec31e | static_analysis |
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
