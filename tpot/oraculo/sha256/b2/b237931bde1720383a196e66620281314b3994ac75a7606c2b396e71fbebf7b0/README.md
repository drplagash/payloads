# 🧬 Payload Analysis

`b237931bde1720383a196e66620281314b3994ac75a7606c2b396e71fbebf7b0`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b237931bde1720383a196e66620281314b3994ac75a7606c2b396e71fbebf7b0`
- **SHA1:** `2c074a0141e829f07a8b4838cb002dd3e1ad1398`
- **MD5:** `fa749ede4c6fc0f0ef5d6a335ff1a21d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (403), with CRLF line terminators |
| Tamaño | 998 B |
| Entropía | 5.53 |
| Strings | 16 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (403), with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 45.153.34.XXX | static_analysis |
| hash | b237931bde1720383a196e66620281314b3994ac75a7606c2b396e71fbebf7b0 | static_analysis |
| ip | 193.26.115.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
