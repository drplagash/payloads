# 🧬 Payload Analysis

`e2bf5e3c09efa5e85d8bfca7aeeb47871d08616f976b0eec0fd00a336872b0e7`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:24:17+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e2bf5e3c09efa5e85d8bfca7aeeb47871d08616f976b0eec0fd00a336872b0e7`
- **SHA1:** `7b6d018edc2c81798c8ff74c2bbf428ab4827fa8`
- **MD5:** `b0d3df8dec8446cd9b99b9b85ac90762`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 118 B |
| Entropía | 4.92 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| hash | e2bf5e3c09efa5e85d8bfca7aeeb47871d08616f976b0eec0fd00a336872b0e7 | static_analysis |
| ip | 206.81.19.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
