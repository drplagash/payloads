# 🧬 Payload Analysis

`b7431ff1c2ac7b4ac37f0107c91fdaafa3e7853280a8b16ba7b998c6bf53bdd4`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:55:35+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b7431ff1c2ac7b4ac37f0107c91fdaafa3e7853280a8b16ba7b998c6bf53bdd4`
- **SHA1:** `6dc37f37686b2ac3b017ab9e278bd7a61e58f296`
- **MD5:** `967bca292144f25b71a1d89ee227dfec`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 19 B |
| Entropía | 3.33 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | b7431ff1c2ac7b4ac37f0107c91fdaafa3e7853280a8b16ba7b998c6bf53bdd4 | static_analysis |
| ip | 45.156.128.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
