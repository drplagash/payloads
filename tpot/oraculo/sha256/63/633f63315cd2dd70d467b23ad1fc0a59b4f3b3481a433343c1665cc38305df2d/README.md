# 🧬 Payload Analysis

`633f63315cd2dd70d467b23ad1fc0a59b4f3b3481a433343c1665cc38305df2d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `633f63315cd2dd70d467b23ad1fc0a59b4f3b3481a433343c1665cc38305df2d`
- **SHA1:** `7c0afd8506883a1b13ada1b0074987f9d1e7607a`
- **MD5:** `6514ad7b9dc6ab723575518dfb2d2d33`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 791 B |
| Entropía | 5.5 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 186.19.59.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 633f63315cd2dd70d467b23ad1fc0a59b4f3b3481a433343c1665cc38305df2d | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
