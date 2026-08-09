# 🧬 Payload Analysis

`1320863100104adbd3dc225e951fac24097d38dbf6b1e6d77243dfb8d8f0e4c8`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:16:33+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1320863100104adbd3dc225e951fac24097d38dbf6b1e6d77243dfb8d8f0e4c8`
- **SHA1:** `ceb72658f2fac4fc6e36dd74e7019c34d50a47d5`
- **MD5:** `2a1d8f37ebb37386c3f538f7cb7b5d15`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 101 B |
| Entropía | 5.08 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.153.XXX | static_analysis |
| hash | 1320863100104adbd3dc225e951fac24097d38dbf6b1e6d77243dfb8d8f0e4c8 | static_analysis |
| ip | 31.59.160.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
