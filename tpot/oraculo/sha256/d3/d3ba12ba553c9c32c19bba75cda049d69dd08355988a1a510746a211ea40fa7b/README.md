# 🧬 Payload Analysis

`d3ba12ba553c9c32c19bba75cda049d69dd08355988a1a510746a211ea40fa7b`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d3ba12ba553c9c32c19bba75cda049d69dd08355988a1a510746a211ea40fa7b`
- **SHA1:** `5ff59aa10260def8793c6a59db23a96f87849252`
- **MD5:** `ec8c25233faf530bdef3d5ef317228a4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 803 B |
| Entropía | 5.48 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 111.107.212.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | d3ba12ba553c9c32c19bba75cda049d69dd08355988a1a510746a211ea40fa7b | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
