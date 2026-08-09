# 🧬 Payload Analysis

`6072b6a46327eb0e6f4144b85ef8d92f84f60b8f6fe529fe49f0a7fe89fda327`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Alta`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:27:00+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6072b6a46327eb0e6f4144b85ef8d92f84f60b8f6fe529fe49f0a7fe89fda327`
- **MD5:** `a30621d85e6954fedcdd989e98c2a178`

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
| hash | 6072b6a46327eb0e6f4144b85ef8d92f84f60b8f6fe529fe49f0a7fe89fda327 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_BusyBox_Mirai |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
