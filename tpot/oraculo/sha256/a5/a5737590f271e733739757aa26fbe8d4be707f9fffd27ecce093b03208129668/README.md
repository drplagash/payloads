# 🧬 Payload Analysis

`a5737590f271e733739757aa26fbe8d4be707f9fffd27ecce093b03208129668`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a5737590f271e733739757aa26fbe8d4be707f9fffd27ecce093b03208129668`
- **SHA1:** `c15e08b0f880e882908643beba4e408f3ddf59c1`
- **MD5:** `b15f592d115ed92d3df4d8a2de74d129`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 801 B |
| Entropía | 5.47 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 110.58.156.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | a5737590f271e733739757aa26fbe8d4be707f9fffd27ecce093b03208129668 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
