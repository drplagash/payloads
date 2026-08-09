# 🧬 Payload Analysis

`9bd66d499797c139ba5d81886a50ebdcdd095fcee3ca4eb940531fca3d978141`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9bd66d499797c139ba5d81886a50ebdcdd095fcee3ca4eb940531fca3d978141`
- **SHA1:** `66cfc6b639abac9d48f69d8410d77b0b2f6a1a9c`
- **MD5:** `caad34622b4973a8df0db13a6803767c`

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
| ip | 176.154.78.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 9bd66d499797c139ba5d81886a50ebdcdd095fcee3ca4eb940531fca3d978141 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
