# 🧬 Payload Analysis

`050223f4f9332ccfc23a62cd5f70a7991d0fb645977de468c6799284d0e19834`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:08:37+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `050223f4f9332ccfc23a62cd5f70a7991d0fb645977de468c6799284d0e19834`
- **SHA1:** `ecad5718d0064d4861c1405adf44e661f3b04a68`
- **MD5:** `3b0a63c9ba07ed03fc7ef5f70421c086`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 198 B |
| Entropía | 5.34 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.166.XXX | static_analysis |
| hash | 050223f4f9332ccfc23a62cd5f70a7991d0fb645977de468c6799284d0e19834 | static_analysis |
| ip | 27.18.70.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
