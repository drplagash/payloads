# 🧬 Payload Analysis

`d7953e6d3c4fb7060ecad84605b32486eca332178ba019e20842dcc07e5b21ca`

## 📌 Resumen

Texto ASCII de 1.4 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `ns` en `hxxp://ogp[.]me/ns`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/d7953e6d3c4fb7060ecad84605b32486eca332178ba019e20842dcc07e5b21ca.md](../../../../../malware-like/oraculo/downloader/d7953e6d3c4fb7060ecad84605b32486eca332178ba019e20842dcc07e5b21ca.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d7953e6d3c4fb7060ecad84605b32486eca332178ba019e20842dcc07e5b21ca`
- **SHA1:** `b2e90444ffb74dd5c3c728f8eed6760285dfd17d`
- **MD5:** `0b22958eb5dd1aa78d5d6f206e36b4f4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | HTML document, ASCII text, with very long lines (399), with CRLF, LF line terminators |
| Tamaño | 1.4 KiB |
| Entropía | 5.46 |
| Strings | 20 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=HTML document, ASCII text, with very long lines (399), with CRLF, LF line terminators; iocs=10

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://ogp[.]me/ns# | strings |
| url | hxxp://schema[.]org/ | strings |
| url | hxxp://www[.]w3[.]org/2000/01/rdf-schema# | strings |
| url | hxxp://rdfs[.]org/sioc/types# | strings |
| url | hxxps://www[.]drupal[.]org) | strings |
| url | hxxp://xmlns[.]com/foaf/0.1/ | strings |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema# | strings |
| url | hxxp://www[.]w3[.]org/2004/02/skos/core# | strings |
| url | hxxp://purl[.]org/dc/terms/ | strings |
| url | hxxp://rdfs[.]org/sioc/ns# | strings |
| url | hxxp://purl[.]org/rss/1.0/modules/content/ | strings |
| hash | d7953e6d3c4fb7060ecad84605b32486eca332178ba019e20842dcc07e5b21ca | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
