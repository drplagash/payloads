# 🧬 Payload Analysis

`117ead67d82dc72684cd49d331170949c557c07a37a19678d398a337dcf2ee84`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `117ead67d82dc72684cd49d331170949c557c07a37a19678d398a337dcf2ee84`
- **SHA1:** `9eae8a3f3f267cdaa14bb33bfea4fc1b82f6fc2f`
- **MD5:** `0ba8c0e87fb7f3c5eb07017bdb8ad5a9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.47 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 109.137.170.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 117ead67d82dc72684cd49d331170949c557c07a37a19678d398a337dcf2ee84 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
