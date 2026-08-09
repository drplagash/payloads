# 🧬 Payload Analysis

`7e3212eb80740af08b92af5da9c8a5379e08cbcbfb10f2e08f176c3333de9734`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7e3212eb80740af08b92af5da9c8a5379e08cbcbfb10f2e08f176c3333de9734`
- **SHA1:** `84680465e9bdfbc06f6f0703435b95e535a88097`
- **MD5:** `0cf7a04298c07194bd1a2f0beaed6568`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Unicode text, UTF-8 text, with CRLF line terminators |
| Tamaño | 1.1 KiB |
| Entropía | 5.59 |
| Strings | 35 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Unicode text, UTF-8 text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.0.11.XXX | static_analysis |
| ip | 160.119.71.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 7e3212eb80740af08b92af5da9c8a5379e08cbcbfb10f2e08f176c3333de9734 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
