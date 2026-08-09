# 🧬 Payload Analysis

`fadcb3a47e6de67c38f0df7ab639d6b961d13367399a0bc72fdd9c8c63739037`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fadcb3a47e6de67c38f0df7ab639d6b961d13367399a0bc72fdd9c8c63739037`
- **SHA1:** `c8766b568a90a0d745026f46b120ef56cf9bd9fc`
- **MD5:** `7d7be74dc32b8c04eeb532b4c06564fe`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 797 B |
| Entropía | 5.49 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 18.205.171.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | fadcb3a47e6de67c38f0df7ab639d6b961d13367399a0bc72fdd9c8c63739037 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
