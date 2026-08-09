# 🧬 Payload Analysis

`8f11570b2e2b66d4e745d30d4b0628d616a1b48e5db68fc34b21c0e03dbb80e1`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8f11570b2e2b66d4e745d30d4b0628d616a1b48e5db68fc34b21c0e03dbb80e1`
- **SHA1:** `094015050418a37cae8379eeb407789f280727fc`
- **MD5:** `ab1b7646e2cb0de85c9a2e3e51b29d79`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.0 KiB |
| Entropía | 5.43 |
| Strings | 33 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 172.86.119.XXX | static_analysis |
| ip | 190.179.140.XXX | static_analysis |
| hash | 8f11570b2e2b66d4e745d30d4b0628d616a1b48e5db68fc34b21c0e03dbb80e1 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
