# 🧬 Payload Analysis

`07a3e70dcffa119d8e3f4a4b96ee60588529bd6c22b289dc2d7463e57e21823b`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `07a3e70dcffa119d8e3f4a4b96ee60588529bd6c22b289dc2d7463e57e21823b`
- **SHA1:** `5e485f92049c1c0d5ca9170e6e2c3629b6fac5eb`
- **MD5:** `dbee60c5cab5393aadf604c091ed007a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 793 B |
| Entropía | 5.49 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 17.207.104.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 07a3e70dcffa119d8e3f4a4b96ee60588529bd6c22b289dc2d7463e57e21823b | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
