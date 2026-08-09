# 🧬 Payload Analysis

`ab983ee90acc2f092e5bc94d7e8acb2d50c4be58236baba11615040e7ea440be`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:19:44+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ab983ee90acc2f092e5bc94d7e8acb2d50c4be58236baba11615040e7ea440be`
- **SHA1:** `38dd8eca139d02ff43c268b8295eaa2b5faca030`
- **MD5:** `f88f5a741fee98b18939665a91b2e38b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (403), with CRLF line terminators |
| Tamaño | 694 B |
| Entropía | 5.37 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (403), with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 45.153.34.XXX | static_analysis |
| hash | ab983ee90acc2f092e5bc94d7e8acb2d50c4be58236baba11615040e7ea440be | static_analysis |
| ip | 45.94.31.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
