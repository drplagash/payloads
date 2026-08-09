# 🧬 Payload Analysis

`0c4ecbc58ffd090458d2df169546f5eb23cbcd6c8225f596ffa2639d0c8b57f5`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0c4ecbc58ffd090458d2df169546f5eb23cbcd6c8225f596ffa2639d0c8b57f5`
- **SHA1:** `10e4f6762cca4906582ef9b47978824f5788990e`
- **MD5:** `b8908442c996dfb61fdea5be68b26ca8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.49 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 177.221.159.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 0c4ecbc58ffd090458d2df169546f5eb23cbcd6c8225f596ffa2639d0c8b57f5 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
