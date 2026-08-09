# 🧬 Payload Analysis

`f76a97bbfb83955196cd9fe353de12d3b67753fc1a00677d64efa64a1f25df91`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:10+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f76a97bbfb83955196cd9fe353de12d3b67753fc1a00677d64efa64a1f25df91`
- **SHA1:** `27b7a78c12618091edadf7e14316e8fc9c13a5c8`
- **MD5:** `cc45bb3cc9a12885ed389a408920c770`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.2 KiB |
| Entropía | 5.36 |
| Strings | 38 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 107.189.24.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | f76a97bbfb83955196cd9fe353de12d3b67753fc1a00677d64efa64a1f25df91 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
