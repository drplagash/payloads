# 🧬 Payload Analysis

`f6da9f5ce86f4c11c3d424b7020ce68973dec45231d2c4f2c42f26d84e99d659`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/f6da9f5ce86f4c11c3d424b7020ce68973dec45231d2c4f2c42f26d84e99d659.md](../../../../../malware-like/oraculo/botnet/f6da9f5ce86f4c11c3d424b7020ce68973dec45231d2c4f2c42f26d84e99d659.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f6da9f5ce86f4c11c3d424b7020ce68973dec45231d2c4f2c42f26d84e99d659`
- **MD5:** `5ddab94efea315b5f4b54e91f6c76014`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 3.8 KiB |
| Entropía | 5.39 |
| Strings | 78 |

## 🔬 Evidencia de clasificación

- Mirai-like indicators in strings
Mirai-like indicators in strings

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | f6da9f5ce86f4c11c3d424b7020ce68973dec45231d2c4f2c42f26d84e99d659 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers3 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
