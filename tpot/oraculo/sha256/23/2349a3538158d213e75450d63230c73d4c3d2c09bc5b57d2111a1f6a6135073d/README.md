# 🧬 Payload Analysis

`2349a3538158d213e75450d63230c73d4c3d2c09bc5b57d2111a1f6a6135073d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2349a3538158d213e75450d63230c73d4c3d2c09bc5b57d2111a1f6a6135073d`
- **SHA1:** `e778c92e6f13e1d682a65e9c8a157cb4d6b2a1a6`
- **MD5:** `7d2e5064bd8d5e149c75280e75050d20`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 805 B |
| Entropía | 5.48 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 151.142.186.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 2349a3538158d213e75450d63230c73d4c3d2c09bc5b57d2111a1f6a6135073d | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
