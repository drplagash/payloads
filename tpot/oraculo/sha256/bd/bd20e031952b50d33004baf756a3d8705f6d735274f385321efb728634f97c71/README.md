# 🧬 Payload Analysis

`bd20e031952b50d33004baf756a3d8705f6d735274f385321efb728634f97c71`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:40+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bd20e031952b50d33004baf756a3d8705f6d735274f385321efb728634f97c71`
- **SHA1:** `b79ea822499ac85828e2fba12c7b3e94de8d07f0`
- **MD5:** `3faf348d01cdf2b67c08d08d5919fc1a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 415 B |
| Entropía | 5.4 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 162.217.103.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| hash | bd20e031952b50d33004baf756a3d8705f6d735274f385321efb728634f97c71 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
