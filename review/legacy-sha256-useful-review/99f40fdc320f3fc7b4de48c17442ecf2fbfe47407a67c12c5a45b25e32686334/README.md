# 🧬 Payload Analysis

`99f40fdc320f3fc7b4de48c17442ecf2fbfe47407a67c12c5a45b25e32686334`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/99f40fdc320f3fc7b4de48c17442ecf2fbfe47407a67c12c5a45b25e32686334.md](../../../../../malware-like/oraculo/botnet/99f40fdc320f3fc7b4de48c17442ecf2fbfe47407a67c12c5a45b25e32686334.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `99f40fdc320f3fc7b4de48c17442ecf2fbfe47407a67c12c5a45b25e32686334`
- **MD5:** `604b8b48845c7cdc9e758a90c92a66af`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 3.6 KiB |
| Entropía | 5.39 |
| Strings | 73 |

## 🔬 Evidencia de clasificación

- Mirai-like indicators in strings
Mirai-like indicators in strings

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 99f40fdc320f3fc7b4de48c17442ecf2fbfe47407a67c12c5a45b25e32686334 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers3 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
