# 🧬 Payload Analysis

`24d68e3e0d5fd13aaf52fc46d08ac209ed56ae212c4ff6ab0d4b8733bf06da44`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `24d68e3e0d5fd13aaf52fc46d08ac209ed56ae212c4ff6ab0d4b8733bf06da44`
- **SHA1:** `e4e7b29ec2d7af6a5012bcbbdd5f588af031db97`
- **MD5:** `79025fc52e67342a733780604aae5070`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 862 B |
| Entropía | 5.56 |
| Strings | 24 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.139.XXX | static_analysis |
| ip | 216.126.224.XXX | static_analysis |
| hash | 24d68e3e0d5fd13aaf52fc46d08ac209ed56ae212c4ff6ab0d4b8733bf06da44 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
