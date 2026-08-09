# 🧬 Payload Analysis

`1a1085e1cd349b7ccfc46f5d30e24eec3fd2bb30a429671d557f9994412e7c43`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1a1085e1cd349b7ccfc46f5d30e24eec3fd2bb30a429671d557f9994412e7c43`
- **SHA1:** `435246c32f28f1001f3effd5bbf37e293db28e55`
- **MD5:** `3b3b1fdb9d5d4e6ffde20dc0bb5bfe72`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 805 B |
| Entropía | 5.46 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 160.157.190.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 1a1085e1cd349b7ccfc46f5d30e24eec3fd2bb30a429671d557f9994412e7c43 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
