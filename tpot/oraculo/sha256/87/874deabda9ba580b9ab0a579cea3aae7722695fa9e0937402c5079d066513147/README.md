# 🧬 Payload Analysis

`874deabda9ba580b9ab0a579cea3aae7722695fa9e0937402c5079d066513147`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:01:51+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `874deabda9ba580b9ab0a579cea3aae7722695fa9e0937402c5079d066513147`
- **SHA1:** `1d3b4f02f95f7cc01c53507c2a6bd81477686e8e`
- **MD5:** `640ba25d47af5c9fa9e281ef8c29b02d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.9 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 239.255.255.XXX | static_analysis |
| hash | 874deabda9ba580b9ab0a579cea3aae7722695fa9e0937402c5079d066513147 | static_analysis |
| ip | 45.194.67.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
