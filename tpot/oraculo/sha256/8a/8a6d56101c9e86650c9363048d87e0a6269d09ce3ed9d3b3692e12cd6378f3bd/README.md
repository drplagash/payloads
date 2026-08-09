# 🧬 Payload Analysis

`8a6d56101c9e86650c9363048d87e0a6269d09ce3ed9d3b3692e12cd6378f3bd`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8a6d56101c9e86650c9363048d87e0a6269d09ce3ed9d3b3692e12cd6378f3bd`
- **SHA1:** `13c29115d60e3b7d34c46c4f8f21f10206481607`
- **MD5:** `428015d0c37b4db9f39eef2a045159eb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 864 B |
| Entropía | 5.58 |
| Strings | 24 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.139.XXX | static_analysis |
| ip | 216.126.224.XXX | static_analysis |
| hash | 8a6d56101c9e86650c9363048d87e0a6269d09ce3ed9d3b3692e12cd6378f3bd | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
