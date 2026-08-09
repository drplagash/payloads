# 🧬 Payload Analysis

`33dd37eea64a0fccf693c16aa34087a929f90ba9470ff55ade13a95dcf9b26f6`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:10+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `33dd37eea64a0fccf693c16aa34087a929f90ba9470ff55ade13a95dcf9b26f6`
- **SHA1:** `a1d8d1de82f1ca6aa2b33c0dba18205d7bd9453c`
- **MD5:** `ffeee42786d76ffec06e19f82f3eb903`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 512 B |
| Entropía | 5.69 |
| Strings | 13 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | 33dd37eea64a0fccf693c16aa34087a929f90ba9470ff55ade13a95dcf9b26f6 | static_analysis |
| ip | 107.189.24.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
