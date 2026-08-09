# 🧬 Payload Analysis

`71e7a933f20017673990be386bfdd587b33a8706b3594d80bdefe760f83fc274`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `71e7a933f20017673990be386bfdd587b33a8706b3594d80bdefe760f83fc274`
- **SHA1:** `ce43a84d2d1f0955e1ccf15721a7eb6cc4291d6d`
- **MD5:** `4a16c109d8cd99d54fac901420b602f6`

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
| ip | 132.30.143.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 71e7a933f20017673990be386bfdd587b33a8706b3594d80bdefe760f83fc274 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
