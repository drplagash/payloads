# 🧬 Payload Analysis

`f27c526236a1ff28ffe0cf032823be07ba45133f7e2f275a77e4313fb6fca86a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:08:37+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f27c526236a1ff28ffe0cf032823be07ba45133f7e2f275a77e4313fb6fca86a`
- **SHA1:** `2ef1f5f65019f9ee27150938499a2208b9762e7e`
- **MD5:** `4846935a4871ef70c7a7fead4d29c411`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (404), with CRLF line terminators |
| Tamaño | 695 B |
| Entropía | 5.38 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (404), with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 204.10.194.XXX | static_analysis |
| hash | f27c526236a1ff28ffe0cf032823be07ba45133f7e2f275a77e4313fb6fca86a | static_analysis |
| ip | 124.198.131.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
