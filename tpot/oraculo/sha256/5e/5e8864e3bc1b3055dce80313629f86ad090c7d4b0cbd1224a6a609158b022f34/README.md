# 🧬 Payload Analysis

`5e8864e3bc1b3055dce80313629f86ad090c7d4b0cbd1224a6a609158b022f34`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: High entropy obfuscation, Binary execution. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:03:26+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5e8864e3bc1b3055dce80313629f86ad090c7d4b0cbd1224a6a609158b022f34`
- **SHA1:** `ed73bc72d8610a385eb105823762f59f70d825bf`
- **MD5:** `5bda613222ecb3ed5723f32c12ca1f36`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0xe9eb0da8 2a79f721 |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **High entropy obfuscation**
2. **Binary execution**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0xe9eb0da8 2a79f721; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 5e8864e3bc1b3055dce80313629f86ad090c7d4b0cbd1224a6a609158b022f34 | static_analysis |
| ip | 37.57.94.XXX | artifact_source |

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
