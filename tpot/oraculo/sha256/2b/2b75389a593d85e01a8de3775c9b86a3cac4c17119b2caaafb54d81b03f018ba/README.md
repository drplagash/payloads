# 🧬 Payload Analysis

`2b75389a593d85e01a8de3775c9b86a3cac4c17119b2caaafb54d81b03f018ba`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:57:27+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2b75389a593d85e01a8de3775c9b86a3cac4c17119b2caaafb54d81b03f018ba`
- **SHA1:** `bd893b01c2731dcde6c6c4259befd7a3841340e4`
- **MD5:** `fe4114969a14a3b23fb32bc9099adb04`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 28 B |
| Entropía | 3.95 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 2b75389a593d85e01a8de3775c9b86a3cac4c17119b2caaafb54d81b03f018ba | static_analysis |
| ip | 45.148.10.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
