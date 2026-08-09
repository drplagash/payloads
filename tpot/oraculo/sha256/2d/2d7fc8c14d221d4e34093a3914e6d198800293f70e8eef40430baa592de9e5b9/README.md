# 🧬 Payload Analysis

`2d7fc8c14d221d4e34093a3914e6d198800293f70e8eef40430baa592de9e5b9`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:22:20+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2d7fc8c14d221d4e34093a3914e6d198800293f70e8eef40430baa592de9e5b9`
- **SHA1:** `9ba80763ac7fe0a732ae6a5f98b3d7926bb6609f`
- **MD5:** `15b08ccfba718fec8aec1b96ed047c0c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 420 B |
| Entropía | 5.39 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 15.204.184.XXX | static_analysis |
| ip | 190.179.128.XXX | static_analysis |
| hash | 2d7fc8c14d221d4e34093a3914e6d198800293f70e8eef40430baa592de9e5b9 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
