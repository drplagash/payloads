# 🧬 Payload Analysis

`4bcc9ea4b86ed6a129bf8d224798ab0b96fc158f182c773029fa1076580810b0`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4bcc9ea4b86ed6a129bf8d224798ab0b96fc158f182c773029fa1076580810b0`
- **SHA1:** `eaeccceae8182977654fc144b1a4bc65962092ec`
- **MD5:** `fb99a28646b9f2d4f3a86aeaed469f30`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.62 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=8

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://ogp[.]me/ns# | strings |
| url | hxxp://purl[.]org/dc/terms/ | strings |
| url | hxxp://purl[.]org/rss/1.0/modules/content/ | strings |
| url | hxxp://rd | strings |
| url | hxxp://schema[.]org/ | strings |
| url | hxxp://www[.]w3[.]org/2000/01/rdf-schema# | strings |
| url | hxxp://xmlns[.]com/foaf/0.1/ | strings |
| hash | 4bcc9ea4b86ed6a129bf8d224798ab0b96fc158f182c773029fa1076580810b0 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
