# 🧬 Payload Analysis

`f5ee890465006fafbae6e8b230b0a463d89960c7b283f69d5a7aed4c5c6da466`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:39:48.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f5ee890465006fafbae6e8b230b0a463d89960c7b283f69d5a7aed4c5c6da466`
- **MD5:** `820e028adb10318e9415b80561aac2a8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (856), with CRLF line terminators |
| Tamaño | 1.0 KiB |
| Entropía | 5.47 |
| Strings | 7 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| ip | 45.153.34.XXX | static_analysis |
| url | hxxp://45.153.34.XXX/rondo. | strings |
| hash | f5ee890465006fafbae6e8b230b0a463d89960c7b283f69d5a7aed4c5c6da466 | static_analysis |
| ip | 141.98.10.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
