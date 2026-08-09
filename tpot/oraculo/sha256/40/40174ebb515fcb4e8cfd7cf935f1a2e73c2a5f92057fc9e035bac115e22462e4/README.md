# 🧬 Payload Analysis

`40174ebb515fcb4e8cfd7cf935f1a2e73c2a5f92057fc9e035bac115e22462e4`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `40174ebb515fcb4e8cfd7cf935f1a2e73c2a5f92057fc9e035bac115e22462e4`
- **SHA1:** `1fe17143ac9ee3c94a3ed620a323528aa6b6d703`
- **MD5:** `ce1f770531c353b4396568129069ac57`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.52 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 115.61.243.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 40174ebb515fcb4e8cfd7cf935f1a2e73c2a5f92057fc9e035bac115e22462e4 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
