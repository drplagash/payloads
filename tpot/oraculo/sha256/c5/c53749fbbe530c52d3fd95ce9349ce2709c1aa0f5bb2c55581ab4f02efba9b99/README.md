# 🧬 Payload Analysis

`c53749fbbe530c52d3fd95ce9349ce2709c1aa0f5bb2c55581ab4f02efba9b99`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:06:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c53749fbbe530c52d3fd95ce9349ce2709c1aa0f5bb2c55581ab4f02efba9b99`
- **SHA1:** `579935d1413e4124799c3df069c42037b88d4f1d`
- **MD5:** `0481fdc9e3f715680eab62fa194854c4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 129 B |
| Entropía | 5.1 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| hash | c53749fbbe530c52d3fd95ce9349ce2709c1aa0f5bb2c55581ab4f02efba9b99 | static_analysis |
| ip | 220.181.1.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
