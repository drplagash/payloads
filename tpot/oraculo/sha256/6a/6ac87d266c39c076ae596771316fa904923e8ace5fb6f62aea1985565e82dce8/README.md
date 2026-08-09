# 🧬 Payload Analysis

`6ac87d266c39c076ae596771316fa904923e8ace5fb6f62aea1985565e82dce8`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6ac87d266c39c076ae596771316fa904923e8ace5fb6f62aea1985565e82dce8`
- **SHA1:** `02d9ad704da53b63ecf0346ebe9aea1120b7329c`
- **MD5:** `08ea57e3386eee91dd7b52ef5a66954b`

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
| ip | 116.128.58.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 6ac87d266c39c076ae596771316fa904923e8ace5fb6f62aea1985565e82dce8 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
