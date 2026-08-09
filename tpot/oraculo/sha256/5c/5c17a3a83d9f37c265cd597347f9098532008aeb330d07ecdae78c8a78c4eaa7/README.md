# 🧬 Payload Analysis

`5c17a3a83d9f37c265cd597347f9098532008aeb330d07ecdae78c8a78c4eaa7`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:57:27+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5c17a3a83d9f37c265cd597347f9098532008aeb330d07ecdae78c8a78c4eaa7`
- **SHA1:** `5958e39ee67da438330acc9bf85c631eb8679411`
- **MD5:** `f32f13c8d5890fd5f6d861d6c6c487fd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 122 B |
| Entropía | 4.93 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.144.XXX | static_analysis |
| hash | 5c17a3a83d9f37c265cd597347f9098532008aeb330d07ecdae78c8a78c4eaa7 | static_analysis |
| ip | 45.148.10.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
