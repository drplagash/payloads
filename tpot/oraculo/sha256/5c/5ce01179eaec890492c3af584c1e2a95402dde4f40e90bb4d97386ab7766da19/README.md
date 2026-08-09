# 🧬 Payload Analysis

`5ce01179eaec890492c3af584c1e2a95402dde4f40e90bb4d97386ab7766da19`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:23:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5ce01179eaec890492c3af584c1e2a95402dde4f40e90bb4d97386ab7766da19`
- **SHA1:** `77026524002a1207ce0741a1452c64b60cf25fd3`
- **MD5:** `f90c88f0727519408fb75403fdae6718`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 717 B |
| Entropía | 5.4 |
| Strings | 21 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.0.11.XXX | static_analysis |
| ip | 190.179.128.XXX | static_analysis |
| hash | 5ce01179eaec890492c3af584c1e2a95402dde4f40e90bb4d97386ab7766da19 | static_analysis |
| ip | 89.190.156.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
