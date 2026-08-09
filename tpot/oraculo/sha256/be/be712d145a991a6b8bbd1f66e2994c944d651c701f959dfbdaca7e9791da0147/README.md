# 🧬 Payload Analysis

`be712d145a991a6b8bbd1f66e2994c944d651c701f959dfbdaca7e9791da0147`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:06:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `be712d145a991a6b8bbd1f66e2994c944d651c701f959dfbdaca7e9791da0147`
- **SHA1:** `02ad6e9913a77ea51515293fd108612ae109c4de`
- **MD5:** `6bcd42c29e2a2c1918238eb67afb8565`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 116 B |
| Entropía | 5.07 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.160.XXX | static_analysis |
| hash | be712d145a991a6b8bbd1f66e2994c944d651c701f959dfbdaca7e9791da0147 | static_analysis |
| ip | 20.83.27.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
