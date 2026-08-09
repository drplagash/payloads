# 🧬 Payload Analysis

`fa4f439f7495e7f2130a9904c1fcce89723e74a84954d11c6d61e4ff04623213`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Alta`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fa4f439f7495e7f2130a9904c1fcce89723e74a84954d11c6d61e4ff04623213`
- **MD5:** `9f040587894426fc5b72fb7a75fcbe89`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | HTML document, ASCII text, with very long lines (1485), with CRLF, LF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.32 |
| Strings | 40 |

## 🔬 Evidencia de clasificación

- YARA match: mirai
YARA match: mirai

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | fa4f439f7495e7f2130a9904c1fcce89723e74a84954d11c6d61e4ff04623213 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_BusyBox_Mirai |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
