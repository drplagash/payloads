# 🧬 Payload Analysis

`3c6d6cbfd7b528890ff5062f570c9096daa1473060bf1c7fa5b361d96ca2a431`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:07:07+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3c6d6cbfd7b528890ff5062f570c9096daa1473060bf1c7fa5b361d96ca2a431`
- **SHA1:** `e3c1ab8dc39113517bf4f8bde16e27115325b6f2`
- **MD5:** `5129662894e6f3d9e55767e820ec8575`

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
| ip | 167.88.164.XXX | static_analysis |
| ip | 190.179.172.XXX | static_analysis |
| hash | 3c6d6cbfd7b528890ff5062f570c9096daa1473060bf1c7fa5b361d96ca2a431 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
