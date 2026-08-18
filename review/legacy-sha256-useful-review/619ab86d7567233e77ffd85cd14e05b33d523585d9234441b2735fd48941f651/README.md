# 🧬 Payload Analysis

`619ab86d7567233e77ffd85cd14e05b33d523585d9234441b2735fd48941f651`

## 📌 Resumen

Artefacto de 814 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.49. Las detecciones YARA incluyen `Big_Numbers1`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:27:00.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `619ab86d7567233e77ffd85cd14e05b33d523585d9234441b2735fd48941f651`
- **MD5:** `76273346a5b1f851d433f28b611d61eb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 814 B |
| Entropía | 5.49 |
| Strings | 21 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.164.XXX | static_analysis |
| ip | 51.75.142.XXX | static_analysis |
| hash | 619ab86d7567233e77ffd85cd14e05b33d523585d9234441b2735fd48941f651 | static_analysis |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers1 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
