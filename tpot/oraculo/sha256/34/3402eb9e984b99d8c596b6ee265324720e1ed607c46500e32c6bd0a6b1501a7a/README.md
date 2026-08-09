# 🧬 Payload Analysis

`3402eb9e984b99d8c596b6ee265324720e1ed607c46500e32c6bd0a6b1501a7a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:46:43+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3402eb9e984b99d8c596b6ee265324720e1ed607c46500e32c6bd0a6b1501a7a`
- **SHA1:** `3d79425b83b9788673773886e7c419fe939ec0d3`
- **MD5:** `c02b34410411115b9ecd5e1527ea41de`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 101 B |
| Entropía | 5.1 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.163.XXX | static_analysis |
| hash | 3402eb9e984b99d8c596b6ee265324720e1ed607c46500e32c6bd0a6b1501a7a | static_analysis |
| ip | 31.59.160.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
