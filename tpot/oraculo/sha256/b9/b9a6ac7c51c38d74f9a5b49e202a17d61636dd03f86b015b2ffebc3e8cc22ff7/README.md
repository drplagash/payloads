# 🧬 Payload Analysis

`b9a6ac7c51c38d74f9a5b49e202a17d61636dd03f86b015b2ffebc3e8cc22ff7`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:41:51+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b9a6ac7c51c38d74f9a5b49e202a17d61636dd03f86b015b2ffebc3e8cc22ff7`
- **SHA1:** `2311e230f7b0056c3fd59de167a3c7ec6296af33`
- **MD5:** `f0285a3fd27e6a755805e0f192692de7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 117 B |
| Entropía | 5.15 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.166.XXX | static_analysis |
| hash | b9a6ac7c51c38d74f9a5b49e202a17d61636dd03f86b015b2ffebc3e8cc22ff7 | static_analysis |
| ip | 40.124.173.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
