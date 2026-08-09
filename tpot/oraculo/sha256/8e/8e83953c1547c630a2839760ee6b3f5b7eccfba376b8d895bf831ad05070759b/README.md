# 🧬 Payload Analysis

`8e83953c1547c630a2839760ee6b3f5b7eccfba376b8d895bf831ad05070759b`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:10:14+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8e83953c1547c630a2839760ee6b3f5b7eccfba376b8d895bf831ad05070759b`
- **SHA1:** `0d80c28ddabf479d03a32969bd0fab04c0aea5b2`
- **MD5:** `71dc705a970cb54b2ed79efe03bc7996`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 54 B |
| Entropía | 4.62 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 8e83953c1547c630a2839760ee6b3f5b7eccfba376b8d895bf831ad05070759b | static_analysis |
| ip | 195.178.110.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
