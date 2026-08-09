# 🧬 Payload Analysis

`88e30522c98f99c8ac23884a65fcf23e0d4b38d8191b7ed27b364b33f291c145`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `88e30522c98f99c8ac23884a65fcf23e0d4b38d8191b7ed27b364b33f291c145`
- **SHA1:** `0f05e096bc56fad1486139dbfe197cc93bd2a60e`
- **MD5:** `7c63d3d0c475c6454c7e8bdca2742ad0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 801 B |
| Entropía | 5.5 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 121.219.146.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 88e30522c98f99c8ac23884a65fcf23e0d4b38d8191b7ed27b364b33f291c145 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
