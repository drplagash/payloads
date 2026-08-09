# 🧬 Payload Analysis

`40359f64f11d20449544003ecc2fdc4fd7c6d5471b0e7b7783473aae95a937a3`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:39:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `40359f64f11d20449544003ecc2fdc4fd7c6d5471b0e7b7783473aae95a937a3`
- **SHA1:** `e1e52da71d0ea9a5f8451b8c9b125f5aa99582b6`
- **MD5:** `94065b3c55b7a7decac791ff68c8b07d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 194 B |
| Entropía | 5.24 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.166.XXX | static_analysis |
| url | hxxps://www[.]nokia[.]com/genomecrawler) | strings |
| hash | 40359f64f11d20449544003ecc2fdc4fd7c6d5471b0e7b7783473aae95a937a3 | static_analysis |
| ip | 216.180.246.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
