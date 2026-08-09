# 🧬 Payload Analysis

`0737a0f9fef5aa34c10a327e9b6642385c15fe29d494d39f297c54a9372f4c84`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:07+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0737a0f9fef5aa34c10a327e9b6642385c15fe29d494d39f297c54a9372f4c84`
- **SHA1:** `efa96a0469f7388d0d4d87baff1f497f342b4885`
- **MD5:** `769290c13f1e0638269dc6e6bb12f80a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 117 B |
| Entropía | 4.97 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.160.XXX | static_analysis |
| hash | 0737a0f9fef5aa34c10a327e9b6642385c15fe29d494d39f297c54a9372f4c84 | static_analysis |
| ip | 206.189.230.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
