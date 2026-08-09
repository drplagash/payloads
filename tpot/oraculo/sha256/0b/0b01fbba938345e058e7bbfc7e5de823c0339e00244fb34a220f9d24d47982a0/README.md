# 🧬 Payload Analysis

`0b01fbba938345e058e7bbfc7e5de823c0339e00244fb34a220f9d24d47982a0`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:10:14+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0b01fbba938345e058e7bbfc7e5de823c0339e00244fb34a220f9d24d47982a0`
- **SHA1:** `114ead1cb07e8a93162b6948e09d262c7215c09d`
- **MD5:** `9c19cf13beb9aff4cbc1a28f9461b8b8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Non-ISO extended-ASCII text, with no line terminators, with escape sequences |
| Tamaño | 90 B |
| Entropía | 5.63 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Non-ISO extended-ASCII text, with no line terminators, with escape sequences; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 0b01fbba938345e058e7bbfc7e5de823c0339e00244fb34a220f9d24d47982a0 | static_analysis |
| ip | 5.83.143.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
