# 🧬 Payload Analysis

`0ef03c1f49ec7d67c55d92c6288270ec8c5e8b2014a3796a5e59758347b2f4ec`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0ef03c1f49ec7d67c55d92c6288270ec8c5e8b2014a3796a5e59758347b2f4ec`
- **SHA1:** `22a50c626f24fa940845ae561e39ef6d27c08476`
- **MD5:** `3d1dae5191986676c391fc705c59b8ff`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 65 B |
| Entropía | 4.55 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 0ef03c1f49ec7d67c55d92c6288270ec8c5e8b2014a3796a5e59758347b2f4ec | static_analysis |
| ip | 31.56.209.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
