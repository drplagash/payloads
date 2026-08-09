# 🧬 Payload Analysis

`56cd422491667460a7e1d3545b505bee57f31deca45e13fff3fe19a0b0a15028`

## 📌 Resumen

Artefacto de 802 B. Identificación de formato: ASCII text, with very long lines (623), with CRLF line terminators. Entropía registrada: 5.48. Se asociaron 4 indicadores de infraestructura. No hay evidencia suficiente para atribuir una familia ni afirmar capacidades maliciosas concretas.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57.000000Z`
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
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://153.117.26.XXX:39399/Mozi.m | strings |
| ip | 153.117.26.XXX | static_analysis |
| hash | 56cd422491667460a7e1d3545b505bee57f31deca45e13fff3fe19a0b0a15028 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
