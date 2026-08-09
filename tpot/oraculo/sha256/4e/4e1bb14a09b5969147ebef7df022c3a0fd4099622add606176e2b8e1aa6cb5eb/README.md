# 🧬 Payload Analysis

`4e1bb14a09b5969147ebef7df022c3a0fd4099622add606176e2b8e1aa6cb5eb`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4e1bb14a09b5969147ebef7df022c3a0fd4099622add606176e2b8e1aa6cb5eb`
- **SHA1:** `12365221576026040d93007ac19dea86feebb277`
- **MD5:** `eb6187d7c29fb80b73f983cfce9db161`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 795 B |
| Entropía | 5.51 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 103.16.54.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 4e1bb14a09b5969147ebef7df022c3a0fd4099622add606176e2b8e1aa6cb5eb | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
