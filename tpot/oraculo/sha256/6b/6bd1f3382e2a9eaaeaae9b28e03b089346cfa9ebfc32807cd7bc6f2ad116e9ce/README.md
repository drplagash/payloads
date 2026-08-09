# 🧬 Payload Analysis

`6bd1f3382e2a9eaaeaae9b28e03b089346cfa9ebfc32807cd7bc6f2ad116e9ce`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:01:37+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6bd1f3382e2a9eaaeaae9b28e03b089346cfa9ebfc32807cd7bc6f2ad116e9ce`
- **SHA1:** `b65472405ad0be508e382e7d66f9644b092c3cb1`
- **MD5:** `2d3eb8c52d1239655f83abebb3992b42`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 957 B |
| Entropía | 5.66 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 134.0.0.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 6bd1f3382e2a9eaaeaae9b28e03b089346cfa9ebfc32807cd7bc6f2ad116e9ce | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
