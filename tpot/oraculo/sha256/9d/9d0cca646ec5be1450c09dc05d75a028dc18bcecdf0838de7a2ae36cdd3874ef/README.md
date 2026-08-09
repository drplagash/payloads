# 🧬 Payload Analysis

`9d0cca646ec5be1450c09dc05d75a028dc18bcecdf0838de7a2ae36cdd3874ef`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:10+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9d0cca646ec5be1450c09dc05d75a028dc18bcecdf0838de7a2ae36cdd3874ef`
- **SHA1:** `44decdc8190c76b1bf5c119b1de85c10f5142bec`
- **MD5:** `fc4215bfff6bfe4d92a0de2580a9d06f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 510 B |
| Entropía | 5.7 |
| Strings | 13 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | 9d0cca646ec5be1450c09dc05d75a028dc18bcecdf0838de7a2ae36cdd3874ef | static_analysis |
| ip | 107.189.24.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
