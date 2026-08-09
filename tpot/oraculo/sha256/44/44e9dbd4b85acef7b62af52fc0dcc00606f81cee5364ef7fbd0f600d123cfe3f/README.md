# 🧬 Payload Analysis

`44e9dbd4b85acef7b62af52fc0dcc00606f81cee5364ef7fbd0f600d123cfe3f`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:00:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `44e9dbd4b85acef7b62af52fc0dcc00606f81cee5364ef7fbd0f600d123cfe3f`
- **SHA1:** `76a8de61944ef92c6ce22bafba12d4b11b54a4f0`
- **MD5:** `3b5537afd511a4c17d2c744aad4b94d0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 943 B |
| Entropía | 5.53 |
| Strings | 29 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 160.119.71.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 44e9dbd4b85acef7b62af52fc0dcc00606f81cee5364ef7fbd0f600d123cfe3f | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
