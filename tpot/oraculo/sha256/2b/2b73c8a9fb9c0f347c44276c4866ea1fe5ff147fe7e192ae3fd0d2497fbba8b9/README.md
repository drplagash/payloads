# 🧬 Payload Analysis

`2b73c8a9fb9c0f347c44276c4866ea1fe5ff147fe7e192ae3fd0d2497fbba8b9`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:21:42+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2b73c8a9fb9c0f347c44276c4866ea1fe5ff147fe7e192ae3fd0d2497fbba8b9`
- **SHA1:** `0092f0ee79eb06e9c47a9f5b9928b83b4888097f`
- **MD5:** `c2e0865128ac0fe063b2bba72b3cde37`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (404), with CRLF line terminators |
| Tamaño | 953 B |
| Entropía | 5.48 |
| Strings | 16 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (404), with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| ip | 204.10.194.XXX | static_analysis |
| hash | 2b73c8a9fb9c0f347c44276c4866ea1fe5ff147fe7e192ae3fd0d2497fbba8b9 | static_analysis |
| ip | 124.198.131.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
