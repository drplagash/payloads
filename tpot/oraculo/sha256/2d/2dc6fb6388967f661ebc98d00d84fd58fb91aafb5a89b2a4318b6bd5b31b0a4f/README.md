# 🧬 Payload Analysis

`2dc6fb6388967f661ebc98d00d84fd58fb91aafb5a89b2a4318b6bd5b31b0a4f`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:06:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2dc6fb6388967f661ebc98d00d84fd58fb91aafb5a89b2a4318b6bd5b31b0a4f`
- **SHA1:** `9430f89d1567dc93611e380ac396a36257dd49de`
- **MD5:** `ecb584ee5fac83c8eb0eb4111198e9cf`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | HTML document, Unicode text, UTF-8 text, with very long lines (399), with CRLF, LF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.21 |
| Strings | 78 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=HTML document, Unicode text, UTF-8 text, with very long lines (399), with CRLF, LF line terminators; iocs=10

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://ogp[.]me/ns# | strings |
| url | hxxp://purl[.]org/dc/terms/ | strings |
| url | hxxp://purl[.]org/rss/1.0/modules/content/ | strings |
| url | hxxp://rdfs[.]org/sioc/ns# | strings |
| url | hxxp://rdfs[.]org/sioc/types# | strings |
| url | hxxp://schema[.]org/ | strings |
| url | hxxp://www[.]w3[.]org/2000/01/rdf-schema# | strings |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema# | strings |
| url | hxxp://www[.]w3[.]org/2004/02/skos/core# | strings |
| url | hxxp://xmlns[.]com/foaf/0.1/ | strings |
| url | hxxps://www[.]drupal[.]org) | strings |
| hash | 2dc6fb6388967f661ebc98d00d84fd58fb91aafb5a89b2a4318b6bd5b31b0a4f | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
