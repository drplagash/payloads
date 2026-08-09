# 🧬 Payload Analysis

`d8940b000c86c0349dbe6e25d87219b0ddc2b58ecb980bc37cf14539acd36cf1`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:31:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d8940b000c86c0349dbe6e25d87219b0ddc2b58ecb980bc37cf14539acd36cf1`
- **SHA1:** `640a85dbbdd306179ec4e20da1eeeb99a0e0c352`
- **MD5:** `554e21c4fdf2fe3d09ac22893d58511c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Non-ISO extended-ASCII text, with no line terminators, with escape sequences |
| Tamaño | 89 B |
| Entropía | 5.67 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Non-ISO extended-ASCII text, with no line terminators, with escape sequences; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | d8940b000c86c0349dbe6e25d87219b0ddc2b58ecb980bc37cf14539acd36cf1 | static_analysis |
| ip | 5.83.143.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
