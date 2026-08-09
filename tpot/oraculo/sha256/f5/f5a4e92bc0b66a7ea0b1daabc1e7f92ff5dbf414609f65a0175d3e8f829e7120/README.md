# 🧬 Payload Analysis

`f5a4e92bc0b66a7ea0b1daabc1e7f92ff5dbf414609f65a0175d3e8f829e7120`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f5a4e92bc0b66a7ea0b1daabc1e7f92ff5dbf414609f65a0175d3e8f829e7120`
- **SHA1:** `da8a5340ef27f80cc730ec610e725dbf8bf593a2`
- **MD5:** `ebb97c4976e74b7fcf548a1fe54a02ce`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.24 |
| Strings | 29 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.2; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | f5a4e92bc0b66a7ea0b1daabc1e7f92ff5dbf414609f65a0175d3e8f829e7120 | static_analysis |
| ip | 181.47.223.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
