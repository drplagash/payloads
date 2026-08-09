# 🧬 Payload Analysis

`54e547992b5a2f2a4fb8292975109ca395c9a76ec108ed989d16c8cc12bcbbbd`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Alta`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:44:48.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `54e547992b5a2f2a4fb8292975109ca395c9a76ec108ed989d16c8cc12bcbbbd`
- **MD5:** `0d5a0bd5ab991fc866c5ee9462a72018`

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
| hash | 54e547992b5a2f2a4fb8292975109ca395c9a76ec108ed989d16c8cc12bcbbbd | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_BusyBox_Mirai |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
