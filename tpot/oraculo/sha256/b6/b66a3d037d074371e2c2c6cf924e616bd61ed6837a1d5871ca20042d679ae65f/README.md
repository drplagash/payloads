# 🧬 Payload Analysis

`b66a3d037d074371e2c2c6cf924e616bd61ed6837a1d5871ca20042d679ae65f`

## 📌 Resumen

Artefacto de 994 B. Formato identificado como ASCII text, with very long lines (403), with CRLF line terminators. Entropía registrada: 5.52. Las detecciones YARA incluyen `Big_Numbers1`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 3 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T18:41:54.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b66a3d037d074371e2c2c6cf924e616bd61ed6837a1d5871ca20042d679ae65f`
- **MD5:** `06a6b9f2de4efc85a66b0f885f5db3c1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (403), with CRLF line terminators |
| Tamaño | 994 B |
| Entropía | 5.52 |
| Strings | 16 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| ip | 45.153.34.XXX | static_analysis |
| hash | b66a3d037d074371e2c2c6cf924e616bd61ed6837a1d5871ca20042d679ae65f | static_analysis |
| ip | 45.94.31.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers1 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
