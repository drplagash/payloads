# 🧬 Payload Analysis

`6fabdf830ec99a5ea94dc657f229c947749011e6db540afca5169fbaacd0a5cb`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:36:21+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6fabdf830ec99a5ea94dc657f229c947749011e6db540afca5169fbaacd0a5cb`
- **SHA1:** `8990b37668e1667dce9283ab437c034a8e029ff9`
- **MD5:** `6fc02e7843c388a71ead443993a432d1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 311 B |
| Entropía | 5.23 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | 6fabdf830ec99a5ea94dc657f229c947749011e6db540afca5169fbaacd0a5cb | static_analysis |
| ip | 8.211.138.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
