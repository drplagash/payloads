# 🧬 Payload Analysis

`7e715e6d2c33a1961d9d4c7598ad9161677bc1a605c6437f9f2af3aab0a7cdf6`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7e715e6d2c33a1961d9d4c7598ad9161677bc1a605c6437f9f2af3aab0a7cdf6`
- **SHA1:** `babe9e4609369c6885a36c6caba6f0e85956d916`
- **MD5:** `bf01c5f850eaeb86e7d331d469fe6f47`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 801 B |
| Entropía | 5.51 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 109.55.223.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 7e715e6d2c33a1961d9d4c7598ad9161677bc1a605c6437f9f2af3aab0a7cdf6 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
