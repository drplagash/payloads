# 🧬 Payload Analysis

`3ae8ecaf1d0b8c0d19ab3f8a360b53ad9d289de6fe91dd8e103c9093732ec3bd`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:00:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3ae8ecaf1d0b8c0d19ab3f8a360b53ad9d289de6fe91dd8e103c9093732ec3bd`
- **SHA1:** `d4b813418a7358194e2650fdc28ced48ac27b36e`
- **MD5:** `f9d64d680ea4cee057e0a111153ac5eb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.1 KiB |
| Entropía | 5.54 |
| Strings | 33 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 160.119.71.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 3ae8ecaf1d0b8c0d19ab3f8a360b53ad9d289de6fe91dd8e103c9093732ec3bd | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
