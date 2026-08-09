# 🧬 Payload Analysis

`402bc4027015921cfa1e2cc759a4057bd242e3f31a91940fb8552a7fea932ecc`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `402bc4027015921cfa1e2cc759a4057bd242e3f31a91940fb8552a7fea932ecc`
- **MD5:** `16bc58f67cf16408f7ab703420a89c33`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (623), with no line terminators |
| Tamaño | 623 B |
| Entropía | 5.38 |
| Strings | 1 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 153.117.26.XXX | static_analysis |
| url | hxxp://153.117.26.XXX:39399/Mozi.m | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| hash | 402bc4027015921cfa1e2cc759a4057bd242e3f31a91940fb8552a7fea932ecc | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
