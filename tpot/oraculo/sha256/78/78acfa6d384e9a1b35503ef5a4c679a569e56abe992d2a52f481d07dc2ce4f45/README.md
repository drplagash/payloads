# 🧬 Payload Analysis

`78acfa6d384e9a1b35503ef5a4c679a569e56abe992d2a52f481d07dc2ce4f45`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:15:55+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `78acfa6d384e9a1b35503ef5a4c679a569e56abe992d2a52f481d07dc2ce4f45`
- **SHA1:** `eecdeffa29530b146ba5d0ca4b3b36ed4083e04e`
- **MD5:** `641625fa6a6e02c5562cbf545ee84818`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 104 B |
| Entropía | 4.97 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.153.XXX | static_analysis |
| hash | 78acfa6d384e9a1b35503ef5a4c679a569e56abe992d2a52f481d07dc2ce4f45 | static_analysis |
| ip | 176.65.148.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
