# 🧬 Payload Analysis

`40170646c9176e18cb6737d20bf204c136eb96a8ff7e2e815a4c13dc96f66d3f`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:34:59+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `40170646c9176e18cb6737d20bf204c136eb96a8ff7e2e815a4c13dc96f66d3f`
- **SHA1:** `07f47e18ec63d3800781fe07c8c4fbe75dbc9f37`
- **MD5:** `784af13f3dad41d8668da7b78db4acde`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 48 B |
| Entropía | 4.31 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 40170646c9176e18cb6737d20bf204c136eb96a8ff7e2e815a4c13dc96f66d3f | static_analysis |
| ip | 45.198.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
