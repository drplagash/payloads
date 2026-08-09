# 🧬 Payload Analysis

`c1914016a6fa0f1c3e6bc4ed0181e4638160739a74698ccb64a0bd56aeea3c72`

## 📌 Resumen

Artefacto de 548 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `content` en `hxxp://purl[.]org/rss/1.0/modules/content/`. Se extrajeron 7 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c1914016a6fa0f1c3e6bc4ed0181e4638160739a74698ccb64a0bd56aeea3c72`
- **SHA1:** `4e34baca739c418effa65c43f589288accd016f1`
- **MD5:** `1dea4d1426b1257436ed664e73dd6a49`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.66 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=8

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://purl[.]org/rss/1.0/modules/content/ | strings |
| url | hxxp://ogp[.]me/ns# | strings |
| url | hxxp://xmlns[.]com/foaf/0.1/ | strings |
| url | hxxp://rd | strings |
| url | hxxp://www[.]w3[.]org/2000/01/rdf-schema# | strings |
| url | hxxp://schema[.]org/ | strings |
| url | hxxp://purl[.]org/dc/terms/ | strings |
| hash | c1914016a6fa0f1c3e6bc4ed0181e4638160739a74698ccb64a0bd56aeea3c72 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
