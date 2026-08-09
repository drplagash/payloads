# 🧬 Payload Analysis

`4004ef0f9c14b26308cabcb570c420024fc81289f8e386b1c918a817a7cfa5b1`

## 📌 Resumen

Artefacto de 548 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `rdf-schema` en `hxxp://www[.]w3[.]org/2000/01/rdf-schema`. Se extrajeron 8 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:14:00.000000Z`
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
| url | hxxp://www[.]w3[.]org/2000/01/rdf-schema# | strings |
| url | hxxp://purl[.]org/rss/1.0/modules/content/ | strings |
| url | hxxp://rdfs[.]org/sioc/ns# | strings |
| url | hxxp://rdfs[.]or | strings |
| url | hxxp://purl[.]org/dc/terms/ | strings |
| url | hxxp://schema[.]org/ | strings |
| url | hxxp://ogp[.]me/ns# | strings |
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
