# 🧬 Payload Analysis

`f07b2e6a3d4da62f4d86e18364c79d48ac020218698dca704ba7ea569d533d9c`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `core` en `hxxp://www[.]w3[.]org/2004/02/skos/core`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/f07b2e6a3d4da62f4d86e18364c79d48ac020218698dca704ba7ea569d533d9c.md](../../../../../malware-like/oraculo/downloader/f07b2e6a3d4da62f4d86e18364c79d48ac020218698dca704ba7ea569d533d9c.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:53.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f07b2e6a3d4da62f4d86e18364c79d48ac020218698dca704ba7ea569d533d9c`
- **SHA1:** `0ad79b401f936a17d05a54e8cf538e69e1eb6804`
- **MD5:** `ce14dee3c21a3899b08fb1c488442507`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.32 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=10

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]w3[.]org/2004/02/skos/core# | strings |
| url | hxxp://rdfs[.]org/sioc/ns# | strings |
| url | hxxp://schema[.]org/ | strings |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema# | strings |
| url | hxxp://rdfs[.]org/sioc/types# | strings |
| url | hxxp://purl[.]org/rss/1.0/modules/content/ | strings |
| url | hxxp://ogp[.]me/ns# | strings |
| url | hxxps://www[.]drupal[.]org) | strings |
| url | hxxp://xmlns[.]com/foaf/0.1/ | strings |
| url | hxxp://www[.]w3[.]org/2000/01/rdf-schema# | strings |
| url | hxxp://purl[.]org/dc/terms/ | strings |
| hash | f07b2e6a3d4da62f4d86e18364c79d48ac020218698dca704ba7ea569d533d9c | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
