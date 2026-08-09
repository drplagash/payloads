# 🧬 Payload Analysis

`2dc6fb6388967f661ebc98d00d84fd58fb91aafb5a89b2a4318b6bd5b31b0a4f`

## 📌 Resumen

Artefacto identificado como HTML document, Unicode text, UTF-8 text, with very long lines (399), with CRLF, LF line terminators de 4.0 KiB. La evidencia estática disponible identifica capacidad de descarga remota. Se extrajo como destino remoto `hxxps://www[.]drupal[.]org`. Se extrajeron 11 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:06:23.000000Z`
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
| url | hxxps://www[.]drupal[.]org) | strings |
| url | hxxp://schema[.]org/ | strings |
| url | hxxp://ogp[.]me/ns# | strings |
| url | hxxp://rdfs[.]org/sioc/types# | strings |
| url | hxxp://xmlns[.]com/foaf/0.1/ | strings |
| url | hxxp://purl[.]org/rss/1.0/modules/content/ | strings |
| url | hxxp://www[.]w3[.]org/2000/01/rdf-schema# | strings |
| url | hxxp://www[.]w3[.]org/2004/02/skos/core# | strings |
| url | hxxp://purl[.]org/dc/terms/ | strings |
| url | hxxp://rdfs[.]org/sioc/ns# | strings |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema# | strings |
| hash | 2dc6fb6388967f661ebc98d00d84fd58fb91aafb5a89b2a4318b6bd5b31b0a4f | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
