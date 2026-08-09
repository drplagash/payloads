# 🧬 Payload Analysis

`b0b125f68d065ca91fc1c38ae2c77e846c684e4c33fe4e1f4ec1fb46d2a26c78`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b0b125f68d065ca91fc1c38ae2c77e846c684e4c33fe4e1f4ec1fb46d2a26c78`
- **SHA1:** `0d738a1b2191fb3deba66dca74c0ccafad590e56`
- **MD5:** `fa782c568636e88a896b8c557d6533b1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 801 B |
| Entropía | 5.52 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 180.136.73.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | b0b125f68d065ca91fc1c38ae2c77e846c684e4c33fe4e1f4ec1fb46d2a26c78 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
