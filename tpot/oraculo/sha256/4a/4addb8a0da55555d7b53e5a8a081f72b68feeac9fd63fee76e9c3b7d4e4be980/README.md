# 🧬 Payload Analysis

`4addb8a0da55555d7b53e5a8a081f72b68feeac9fd63fee76e9c3b7d4e4be980`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:10+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4addb8a0da55555d7b53e5a8a081f72b68feeac9fd63fee76e9c3b7d4e4be980`
- **SHA1:** `381f6d02dcac552f0c0764989740f5391fdd6c10`
- **MD5:** `b3adf5c6c0ec8d4582fa8e296ff5875f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 512 B |
| Entropía | 5.68 |
| Strings | 13 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | 4addb8a0da55555d7b53e5a8a081f72b68feeac9fd63fee76e9c3b7d4e4be980 | static_analysis |
| ip | 107.189.24.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
