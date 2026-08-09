# 🧬 Payload Analysis

`82438bd5c8dd32e4bc818793b0b2854fbf71b648c74efd983cf67589a09f33c0`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `82438bd5c8dd32e4bc818793b0b2854fbf71b648c74efd983cf67589a09f33c0`
- **SHA1:** `c1b8e076c47e55ea8550209b7cd888da6c083709`
- **MD5:** `fea8e79dbd905f7524ba60f87bdc3f48`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 348 B |
| Entropía | 5.5 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 128.0.0.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| hash | 82438bd5c8dd32e4bc818793b0b2854fbf71b648c74efd983cf67589a09f33c0 | static_analysis |
| ip | 185.93.89.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
