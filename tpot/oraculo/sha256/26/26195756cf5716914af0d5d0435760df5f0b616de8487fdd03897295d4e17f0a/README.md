# 🧬 Payload Analysis

`26195756cf5716914af0d5d0435760df5f0b616de8487fdd03897295d4e17f0a`

## 📌 Resumen

Artefacto de 495 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.58. Las detecciones YARA incluyen `Big_Numbers1`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T18:41:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `26195756cf5716914af0d5d0435760df5f0b616de8487fdd03897295d4e17f0a`
- **MD5:** `5495255d85496565906228570c3fa9bb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 495 B |
| Entropía | 5.58 |
| Strings | 12 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| ip | 199.195.250.XXX | static_analysis |
| hash | 26195756cf5716914af0d5d0435760df5f0b616de8487fdd03897295d4e17f0a | static_analysis |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers1 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
