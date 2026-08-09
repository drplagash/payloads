# 🧬 Payload Analysis

`6f766d2153a766dc6c0d9f745774e833caf1b8ec122e0efc160fcca3b04da4e5`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:20:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6f766d2153a766dc6c0d9f745774e833caf1b8ec122e0efc160fcca3b04da4e5`
- **SHA1:** `a36217dc4d7eb16c9e89178254a5d4a211e636cf`
- **MD5:** `00d92e89509a90c7892048ea619ef2db`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 123 B |
| Entropía | 4.87 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| hash | 6f766d2153a766dc6c0d9f745774e833caf1b8ec122e0efc160fcca3b04da4e5 | static_analysis |
| ip | 45.148.10.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
