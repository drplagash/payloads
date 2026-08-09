# 🧬 Payload Analysis

`bb7a625bf05b71cae19bcaa1aa71de107a5113b726776efef5897febe44935b5`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:14:00+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bb7a625bf05b71cae19bcaa1aa71de107a5113b726776efef5897febe44935b5`
- **SHA1:** `43f6f390ff161478adc0dd5ec07fa1bc69ffd1a5`
- **MD5:** `cc7112763fd3b459f94da920c599254c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 171 B |
| Entropía | 5.13 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.153.XXX | static_analysis |
| hash | bb7a625bf05b71cae19bcaa1aa71de107a5113b726776efef5897febe44935b5 | static_analysis |
| ip | 77.83.240.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
