# 🧬 Payload Analysis

`55904c0447688afaede2ddb5272e9c94ceb551072a146906d9f97b64dde79db6`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:00:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `55904c0447688afaede2ddb5272e9c94ceb551072a146906d9f97b64dde79db6`
- **SHA1:** `8d8c88d4f6ea2a48458b16e911d6a0fb928f2172`
- **MD5:** `0d0b113741e7656f89ffb5cd278771d8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (403), with CRLF line terminators |
| Tamaño | 998 B |
| Entropía | 5.53 |
| Strings | 16 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (403), with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 45.153.34.XXX | static_analysis |
| hash | 55904c0447688afaede2ddb5272e9c94ceb551072a146906d9f97b64dde79db6 | static_analysis |
| ip | 193.26.115.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
