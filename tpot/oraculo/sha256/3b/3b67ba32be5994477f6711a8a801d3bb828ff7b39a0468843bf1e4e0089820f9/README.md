# 🧬 Payload Analysis

`3b67ba32be5994477f6711a8a801d3bb828ff7b39a0468843bf1e4e0089820f9`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3b67ba32be5994477f6711a8a801d3bb828ff7b39a0468843bf1e4e0089820f9`
- **SHA1:** `002faf18d3676c7f8b293fba708f84d26ce2c48b`
- **MD5:** `500013ac1b832db9236073f85188c6e3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.54 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 116.154.94.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 3b67ba32be5994477f6711a8a801d3bb828ff7b39a0468843bf1e4e0089820f9 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
