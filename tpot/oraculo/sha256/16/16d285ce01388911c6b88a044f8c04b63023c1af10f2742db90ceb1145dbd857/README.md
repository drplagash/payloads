# 🧬 Payload Analysis

`16d285ce01388911c6b88a044f8c04b63023c1af10f2742db90ceb1145dbd857`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:08:37+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `16d285ce01388911c6b88a044f8c04b63023c1af10f2742db90ceb1145dbd857`
- **SHA1:** `159225274b3329d90c0679941c26431d01651889`
- **MD5:** `e9ef0241188b51ae8c97fa317e3bc845`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 181 B |
| Entropía | 5.1 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| hash | 16d285ce01388911c6b88a044f8c04b63023c1af10f2742db90ceb1145dbd857 | static_analysis |
| ip | 160.119.76.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
