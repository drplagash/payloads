# 🧬 Payload Analysis

`afcb7b8dbe76629fcd8b45151d2ca68dc56510d9ccae92170587e6af62e972ae`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:16:33+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `afcb7b8dbe76629fcd8b45151d2ca68dc56510d9ccae92170587e6af62e972ae`
- **SHA1:** `e0c34af98884824254a4004f756bf6e50902a5ad`
- **MD5:** `5ad71b11e9f95e63c40eeaf92e6e2713`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 414 B |
| Entropía | 5.37 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 185.243.5.XXX | static_analysis |
| ip | 190.179.153.XXX | static_analysis |
| hash | afcb7b8dbe76629fcd8b45151d2ca68dc56510d9ccae92170587e6af62e972ae | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
