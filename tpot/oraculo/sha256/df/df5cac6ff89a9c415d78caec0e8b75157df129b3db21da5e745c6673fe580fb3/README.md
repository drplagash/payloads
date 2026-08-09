# 🧬 Payload Analysis

`df5cac6ff89a9c415d78caec0e8b75157df129b3db21da5e745c6673fe580fb3`

## 📌 Resumen

Artefacto de 1018 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.16. Las detecciones YARA incluyen `Big_Numbers3`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T18:44:48.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `df5cac6ff89a9c415d78caec0e8b75157df129b3db21da5e745c6673fe580fb3`
- **MD5:** `527dc4b113dbb3ff2c8b9fbe9f658e94`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1018 B |
| Entropía | 5.16 |
| Strings | 30 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.164.XXX | static_analysis |
| ip | 179.43.167.XXX | static_analysis |
| hash | df5cac6ff89a9c415d78caec0e8b75157df129b3db21da5e745c6673fe580fb3 | static_analysis |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers3 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
