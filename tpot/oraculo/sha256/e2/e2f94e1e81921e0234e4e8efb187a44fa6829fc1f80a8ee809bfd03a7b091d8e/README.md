# 🧬 Payload Analysis

`e2f94e1e81921e0234e4e8efb187a44fa6829fc1f80a8ee809bfd03a7b091d8e`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:19:06+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e2f94e1e81921e0234e4e8efb187a44fa6829fc1f80a8ee809bfd03a7b091d8e`
- **SHA1:** `43237bca3fc5e0d170f63283c1bafe4da1cacd4d`
- **MD5:** `ef2900553f32f3def66e254a9d6e23e4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 111 B |
| Entropía | 4.91 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 185.65.245.XXX | static_analysis |
| hash | e2f94e1e81921e0234e4e8efb187a44fa6829fc1f80a8ee809bfd03a7b091d8e | static_analysis |
| ip | 176.65.148.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
