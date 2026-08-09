# 🧬 Payload Analysis

`4041d19ebdee06b395c48ca277dbaa7382af696632e825cf8d543f49c1f8204e`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:48:49+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4041d19ebdee06b395c48ca277dbaa7382af696632e825cf8d543f49c1f8204e`
- **SHA1:** `8597a84e21c1215fe5b42caa977f97e0c2e6dc15`
- **MD5:** `2ee6326cbddfc240aeb093dbf68831f1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 50 B |
| Entropía | 4.48 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 4041d19ebdee06b395c48ca277dbaa7382af696632e825cf8d543f49c1f8204e | static_analysis |
| ip | 176.65.139.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
