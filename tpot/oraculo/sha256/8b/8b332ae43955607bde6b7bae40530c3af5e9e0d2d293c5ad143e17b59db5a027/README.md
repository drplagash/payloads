# 🧬 Payload Analysis

`8b332ae43955607bde6b7bae40530c3af5e9e0d2d293c5ad143e17b59db5a027`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8b332ae43955607bde6b7bae40530c3af5e9e0d2d293c5ad143e17b59db5a027`
- **SHA1:** `66dc81633e0037768b0b5d336403ecc140793303`
- **MD5:** `596ec6ab99804f55912f0f8708c04d3c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 795 B |
| Entropía | 5.48 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 164.88.203.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 8b332ae43955607bde6b7bae40530c3af5e9e0d2d293c5ad143e17b59db5a027 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
