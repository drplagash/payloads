# 🧬 Payload Analysis

`bb13e06e5438487dfd8e08eeef11ce17238756f458f56ecf1d30a993e4ef45b6`

## 📌 Resumen

Artefacto de 812 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.50. Las detecciones YARA incluyen `Big_Numbers1`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:27:00.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bb13e06e5438487dfd8e08eeef11ce17238756f458f56ecf1d30a993e4ef45b6`
- **MD5:** `f9c5cdbad657c3068f3cb56f405fee30`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 812 B |
| Entropía | 5.5 |
| Strings | 21 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.164.XXX | static_analysis |
| ip | 51.75.142.XXX | static_analysis |
| hash | bb13e06e5438487dfd8e08eeef11ce17238756f458f56ecf1d30a993e4ef45b6 | static_analysis |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers1 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
