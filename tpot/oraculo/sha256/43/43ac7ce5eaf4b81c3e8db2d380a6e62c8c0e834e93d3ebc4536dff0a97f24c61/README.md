# 🧬 Payload Analysis

`43ac7ce5eaf4b81c3e8db2d380a6e62c8c0e834e93d3ebc4536dff0a97f24c61`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `43ac7ce5eaf4b81c3e8db2d380a6e62c8c0e834e93d3ebc4536dff0a97f24c61`
- **SHA1:** `efcb5b0e32c0adbe656c1c4568bf893f6c8a118f`
- **MD5:** `a407d75a3e6c5e48027d2b4ba5814e13`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 941 B |
| Entropía | 5.62 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 134.0.0.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| hash | 43ac7ce5eaf4b81c3e8db2d380a6e62c8c0e834e93d3ebc4536dff0a97f24c61 | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
