# 🧬 Payload Analysis

`9a4f41691cac1466ebc60f3e3a152941ec4df3e3757dbd7fd11d8377fa3d69c9`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:00:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9a4f41691cac1466ebc60f3e3a152941ec4df3e3757dbd7fd11d8377fa3d69c9`
- **SHA1:** `d2a09024a0649c75860373bd06310a0680d20044`
- **MD5:** `fb717bb42006e21d1d5834cbbc5239f8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Unicode text, UTF-8 text, with CRLF line terminators |
| Tamaño | 1.1 KiB |
| Entropía | 5.61 |
| Strings | 35 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Unicode text, UTF-8 text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 160.119.71.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 9a4f41691cac1466ebc60f3e3a152941ec4df3e3757dbd7fd11d8377fa3d69c9 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
