# 🧬 Payload Analysis

`b4a420cb0c4b76a962203f13d0be7c2ffd15a839fac6ce449a0e4d742522d708`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:40:04+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b4a420cb0c4b76a962203f13d0be7c2ffd15a839fac6ce449a0e4d742522d708`
- **MD5:** `975ea3c0392d4d5b07d2c04c20418d97`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 410 B |
| Entropía | 5.4 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| hash | b4a420cb0c4b76a962203f13d0be7c2ffd15a839fac6ce449a0e4d742522d708 | static_analysis |
| ip | 87.246.54.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
