# 🧬 Payload Analysis

`d972ea4b58ecdd36b7f6535f9af7a5fd4c0ba1372a0439ddda0522f7423d41f1`

## 📌 Resumen

Artefacto de 997 B. Formato identificado como ASCII text, with very long lines (403), with CRLF line terminators. Entropía registrada: 5.53. Las detecciones YARA incluyen `Big_Numbers1`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 3 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:30:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d972ea4b58ecdd36b7f6535f9af7a5fd4c0ba1372a0439ddda0522f7423d41f1`
- **MD5:** `2c6de0ae81231458280c598ea87c2a82`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (403), with CRLF line terminators |
| Tamaño | 997 B |
| Entropía | 5.53 |
| Strings | 16 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 45.153.34.XXX | static_analysis |
| ip | 190.179.164.XXX | static_analysis |
| hash | d972ea4b58ecdd36b7f6535f9af7a5fd4c0ba1372a0439ddda0522f7423d41f1 | static_analysis |
| ip | 94.154.43.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers1 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
