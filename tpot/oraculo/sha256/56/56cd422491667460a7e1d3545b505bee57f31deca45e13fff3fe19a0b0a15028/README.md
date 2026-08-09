# 🧬 Payload Analysis

`56cd422491667460a7e1d3545b505bee57f31deca45e13fff3fe19a0b0a15028`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `56cd422491667460a7e1d3545b505bee57f31deca45e13fff3fe19a0b0a15028`
- **MD5:** `36ac268ac59cec52f7e5a394d81a56c7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (623), with CRLF line terminators |
| Tamaño | 802 B |
| Entropía | 5.48 |
| Strings | 7 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 153.117.26.XXX | static_analysis |
| url | hxxp://153.117.26.XXX:39399/Mozi.m | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| hash | 56cd422491667460a7e1d3545b505bee57f31deca45e13fff3fe19a0b0a15028 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
