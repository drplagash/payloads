# 🧬 Payload Analysis

`12af84c75a0f71608a88702edb358e5be2911fc966c1028ccac51c9d1a9f9c9f`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:39:31+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `12af84c75a0f71608a88702edb358e5be2911fc966c1028ccac51c9d1a9f9c9f`
- **MD5:** `e045d6eb6a91ad410fa04978283c624e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 314 B |
| Entropía | 5.36 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 144.172.106.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| hash | 12af84c75a0f71608a88702edb358e5be2911fc966c1028ccac51c9d1a9f9c9f | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
