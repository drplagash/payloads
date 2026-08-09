# 🧬 Payload Analysis

`4004ef0f9c14b26308cabcb570c420024fc81289f8e386b1c918a817a7cfa5b1`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:14:00+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4004ef0f9c14b26308cabcb570c420024fc81289f8e386b1c918a817a7cfa5b1`
- **SHA1:** `0e30ba571ed2b9214de662f71d948b3d507b0dd3`
- **MD5:** `6a4f97fb7efb703012f77961ce64e843`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.5 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=9

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://ogp[.]me/ns# | strings |
| url | hxxp://purl[.]org/dc/terms/ | strings |
| url | hxxp://purl[.]org/rss/1.0/modules/content/ | strings |
| url | hxxp://rdfs[.]or | strings |
| url | hxxp://rdfs[.]org/sioc/ns# | strings |
| url | hxxp://schema[.]org/ | strings |
| url | hxxp://www[.]w3[.]org/2000/01/rdf-schema# | strings |
| url | hxxp://xmlns[.]com/foaf/0.1/ | strings |
| hash | 4004ef0f9c14b26308cabcb570c420024fc81289f8e386b1c918a817a7cfa5b1 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
