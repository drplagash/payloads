# 🧬 Payload Analysis

`4aa8d50abcfb2aa24cc1cf95249e0f216e0f0f3917a2728c2e2b0ad6cfdda0de`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:49:32+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4aa8d50abcfb2aa24cc1cf95249e0f216e0f0f3917a2728c2e2b0ad6cfdda0de`
- **SHA1:** `ac8bcb5b3d11634ddaeac206b8aa203876b64f52`
- **MD5:** `43c432a6037882ad1c8d91ca90ab6f6a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 949 B |
| Entropía | 5.66 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 134.0.0.XXX | static_analysis |
| ip | 190.179.144.XXX | static_analysis |
| hash | 4aa8d50abcfb2aa24cc1cf95249e0f216e0f0f3917a2728c2e2b0ad6cfdda0de | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
