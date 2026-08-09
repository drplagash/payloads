# 🧬 Payload Analysis

`497da84ddb212dbef1e510fee157d34f4faca9aa2313b3e887cba01f7dd56262`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:10:07+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `497da84ddb212dbef1e510fee157d34f4faca9aa2313b3e887cba01f7dd56262`
- **SHA1:** `8a4c34e042c815c1134e62e97a83c742f20c7e2b`
- **MD5:** `56331e03d9271017a35ba1de7416f386`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF, LF line terminators |
| Tamaño | 61 B |
| Entropía | 4.72 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF, LF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 497da84ddb212dbef1e510fee157d34f4faca9aa2313b3e887cba01f7dd56262 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
