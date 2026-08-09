# 🧬 Payload Analysis

`8e1f98e9b2eddc6a5bcea18427d7e66843c737bc07994a3375887edb63d24ac2`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8e1f98e9b2eddc6a5bcea18427d7e66843c737bc07994a3375887edb63d24ac2`
- **SHA1:** `f2c09baf1908b6dff3e1190cce518d122a50abf4`
- **MD5:** `dab8a4c76f708504fb8f57a9cbb78bfe`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 797 B |
| Entropía | 5.51 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 154.3.196.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 8e1f98e9b2eddc6a5bcea18427d7e66843c737bc07994a3375887edb63d24ac2 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
