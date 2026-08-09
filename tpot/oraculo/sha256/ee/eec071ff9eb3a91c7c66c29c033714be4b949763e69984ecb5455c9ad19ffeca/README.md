# 🧬 Payload Analysis

`eec071ff9eb3a91c7c66c29c033714be4b949763e69984ecb5455c9ad19ffeca`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:53:04+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `eec071ff9eb3a91c7c66c29c033714be4b949763e69984ecb5455c9ad19ffeca`
- **SHA1:** `9bcf3c552fff7604fb13ff6d4f0627adfb836e70`
- **MD5:** `14c45b9abe5f07b670f7394d92b8c884`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0xeb4ba43e 3d0c0d73 |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0xeb4ba43e 3d0c0d73; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | eec071ff9eb3a91c7c66c29c033714be4b949763e69984ecb5455c9ad19ffeca | static_analysis |
| ip | 202.163.87.XXX | artifact_source |

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
