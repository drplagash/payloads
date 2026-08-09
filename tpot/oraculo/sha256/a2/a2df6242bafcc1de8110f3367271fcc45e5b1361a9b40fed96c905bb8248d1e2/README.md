# 🧬 Payload Analysis

`a2df6242bafcc1de8110f3367271fcc45e5b1361a9b40fed96c905bb8248d1e2`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:09:22+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a2df6242bafcc1de8110f3367271fcc45e5b1361a9b40fed96c905bb8248d1e2`
- **SHA1:** `a942e7216af7d1a2bca400af5ae231cd4c9af06f`
- **MD5:** `478b2efdffd4d01cfa617f909ceba4eb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 92 B |
| Entropía | 4.78 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | a2df6242bafcc1de8110f3367271fcc45e5b1361a9b40fed96c905bb8248d1e2 | static_analysis |
| ip | 185.224.128.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
