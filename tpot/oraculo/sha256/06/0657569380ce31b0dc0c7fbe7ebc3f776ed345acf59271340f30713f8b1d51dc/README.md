# 🧬 Payload Analysis

`0657569380ce31b0dc0c7fbe7ebc3f776ed345acf59271340f30713f8b1d51dc`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:47+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0657569380ce31b0dc0c7fbe7ebc3f776ed345acf59271340f30713f8b1d51dc`
- **MD5:** `832d5023312ee360ae937a693ea65d7a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 404 B |
| Entropía | 5.43 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| hash | 0657569380ce31b0dc0c7fbe7ebc3f776ed345acf59271340f30713f8b1d51dc | static_analysis |
| ip | 198.98.54.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
