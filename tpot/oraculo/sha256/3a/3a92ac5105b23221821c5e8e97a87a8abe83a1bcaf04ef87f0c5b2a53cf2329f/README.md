# 🧬 Payload Analysis

`3a92ac5105b23221821c5e8e97a87a8abe83a1bcaf04ef87f0c5b2a53cf2329f`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:17:49+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3a92ac5105b23221821c5e8e97a87a8abe83a1bcaf04ef87f0c5b2a53cf2329f`
- **SHA1:** `d11622cb1dc26eab7dbbe156a81a8c1057820945`
- **MD5:** `13d9653acb9d8a3eb4ff6d5b35d81184`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 444 B |
| Entropía | 5.55 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| hash | 3a92ac5105b23221821c5e8e97a87a8abe83a1bcaf04ef87f0c5b2a53cf2329f | static_analysis |
| ip | 5.61.209.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
