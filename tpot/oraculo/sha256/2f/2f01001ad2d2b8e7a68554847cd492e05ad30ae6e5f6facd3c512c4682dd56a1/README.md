# 🧬 Payload Analysis

`2f01001ad2d2b8e7a68554847cd492e05ad30ae6e5f6facd3c512c4682dd56a1`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:23:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2f01001ad2d2b8e7a68554847cd492e05ad30ae6e5f6facd3c512c4682dd56a1`
- **SHA1:** `840d7d471b14a676b3d13b7249e0b0227fd8066b`
- **MD5:** `ecd1bbc1f228a7f9f0a39ffafe6e205e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 206 B |
| Entropía | 5.37 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 136.0.0.XXX | static_analysis |
| ip | 190.179.128.XXX | static_analysis |
| hash | 2f01001ad2d2b8e7a68554847cd492e05ad30ae6e5f6facd3c512c4682dd56a1 | static_analysis |
| ip | 52.200.76.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
