# 🧬 Payload Analysis

`5df223900ba1774e840e1aa111ebf0bb835d2ccee3c4de43cacf8f15c63c54a8`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5df223900ba1774e840e1aa111ebf0bb835d2ccee3c4de43cacf8f15c63c54a8`
- **SHA1:** `b6b546daec8ddecff4f98becf6059623379e9372`
- **MD5:** `ec4ff800c7b36782e6fd979eb2aba46e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 340 B |
| Entropía | 5.46 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| hash | 5df223900ba1774e840e1aa111ebf0bb835d2ccee3c4de43cacf8f15c63c54a8 | static_analysis |
| ip | 185.93.89.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
