# 🧬 Payload Analysis

`e3e3a088a83654b14738580ac5a8c7c288c50ced78b1d0da95db78e4648c39d3`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:27:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e3e3a088a83654b14738580ac5a8c7c288c50ced78b1d0da95db78e4648c39d3`
- **SHA1:** `91c7dba3b3d7b237e4011b3be8e821b10d8060fe`
- **MD5:** `e865dd9c62324b9fa4f240423f99a615`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 584 B |
| Entropía | 5.48 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| hash | e3e3a088a83654b14738580ac5a8c7c288c50ced78b1d0da95db78e4648c39d3 | static_analysis |
| ip | 43.135.134.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
