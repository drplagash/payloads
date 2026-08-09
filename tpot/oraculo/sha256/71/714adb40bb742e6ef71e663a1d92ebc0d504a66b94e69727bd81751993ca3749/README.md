# 🧬 Payload Analysis

`714adb40bb742e6ef71e663a1d92ebc0d504a66b94e69727bd81751993ca3749`

## 📌 Resumen

Artefacto de 997 B. Formato identificado como ASCII text, with very long lines (403), with CRLF line terminators. Entropía registrada: 5.52. Las detecciones YARA incluyen `Big_Numbers1`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 3 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `714adb40bb742e6ef71e663a1d92ebc0d504a66b94e69727bd81751993ca3749`
- **MD5:** `145f8047688a8462fd994d85234c95d2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (403), with CRLF line terminators |
| Tamaño | 997 B |
| Entropía | 5.52 |
| Strings | 16 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 45.153.34.XXX | static_analysis |
| ip | 190.179.177.XXX | static_analysis |
| hash | 714adb40bb742e6ef71e663a1d92ebc0d504a66b94e69727bd81751993ca3749 | static_analysis |
| ip | 141.98.10.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers1 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
