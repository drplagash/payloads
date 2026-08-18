# 🧬 Payload Analysis

`6dc1410dbe93a98c1679fbca56c220f40a813b70629c1171cc96af496a5144f5`

## 📌 Resumen

Artefacto de 1003 B. Formato identificado como ASCII text, with very long lines (403), with CRLF line terminators. Entropía registrada: 5.52. Las detecciones YARA incluyen `Big_Numbers1`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 3 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:30:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6dc1410dbe93a98c1679fbca56c220f40a813b70629c1171cc96af496a5144f5`
- **MD5:** `b8141e21278e20a4e00d7d701b710195`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (403), with CRLF line terminators |
| Tamaño | 1003 B |
| Entropía | 5.52 |
| Strings | 16 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 45.153.34.XXX | static_analysis |
| ip | 190.179.164.XXX | static_analysis |
| hash | 6dc1410dbe93a98c1679fbca56c220f40a813b70629c1171cc96af496a5144f5 | static_analysis |
| ip | 94.154.43.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers1 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
