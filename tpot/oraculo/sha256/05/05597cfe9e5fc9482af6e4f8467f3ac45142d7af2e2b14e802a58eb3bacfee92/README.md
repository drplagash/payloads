# 🧬 Payload Analysis

`05597cfe9e5fc9482af6e4f8467f3ac45142d7af2e2b14e802a58eb3bacfee92`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `05597cfe9e5fc9482af6e4f8467f3ac45142d7af2e2b14e802a58eb3bacfee92`
- **SHA1:** `a5e9cd0d358c67514537423a07c9ed5ead592c65`
- **MD5:** `d9e0d7228b990a3173dc588ac09397df`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 117 B |
| Entropía | 5.09 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.139.XXX | static_analysis |
| hash | 05597cfe9e5fc9482af6e4f8467f3ac45142d7af2e2b14e802a58eb3bacfee92 | static_analysis |
| ip | 40.124.170.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
