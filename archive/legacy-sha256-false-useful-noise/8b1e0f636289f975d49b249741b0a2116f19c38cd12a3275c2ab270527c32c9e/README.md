# 🧬 Payload Analysis

`8b1e0f636289f975d49b249741b0a2116f19c38cd12a3275c2ab270527c32c9e`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Infraestructura remota: `hxxps://www[.]drupal[.]org`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/8b1e0f636289f975d49b249741b0a2116f19c38cd12a3275c2ab270527c32c9e.md](../../../../../malware-like/oraculo/downloader/8b1e0f636289f975d49b249741b0a2116f19c38cd12a3275c2ab270527c32c9e.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:06:23.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8b1e0f636289f975d49b249741b0a2116f19c38cd12a3275c2ab270527c32c9e`
- **SHA1:** `780e712909d106704b46f57c8562cceca681f6dd`
- **MD5:** `43675aaaefbc9c12efa7b8d8eb4f4bc2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.33 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=10

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
| hash | 8b1e0f636289f975d49b249741b0a2116f19c38cd12a3275c2ab270527c32c9e | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
