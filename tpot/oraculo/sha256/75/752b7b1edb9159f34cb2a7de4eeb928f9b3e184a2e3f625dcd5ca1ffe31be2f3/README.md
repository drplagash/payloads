# 🧬 Payload Analysis

`752b7b1edb9159f34cb2a7de4eeb928f9b3e184a2e3f625dcd5ca1ffe31be2f3`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:28:55+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `752b7b1edb9159f34cb2a7de4eeb928f9b3e184a2e3f625dcd5ca1ffe31be2f3`
- **SHA1:** `6b86caf8c870fe35e18a8ded10ae792aefeebf57`
- **MD5:** `eb8ea3abcb82ea2f72ff77c00b544666`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 734 B |
| Entropía | 5.34 |
| Strings | 22 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | 752b7b1edb9159f34cb2a7de4eeb928f9b3e184a2e3f625dcd5ca1ffe31be2f3 | static_analysis |
| ip | 87.106.98.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
