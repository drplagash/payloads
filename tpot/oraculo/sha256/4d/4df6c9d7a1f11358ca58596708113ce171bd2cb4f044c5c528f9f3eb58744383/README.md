# 🧬 Payload Analysis

`4df6c9d7a1f11358ca58596708113ce171bd2cb4f044c5c528f9f3eb58744383`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:37:42+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4df6c9d7a1f11358ca58596708113ce171bd2cb4f044c5c528f9f3eb58744383`
- **SHA1:** `b6439c11b1d1c6768bf3e9324cd4b64e05b42190`
- **MD5:** `fc715bdedabb5f46edd864d50f9406f2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.2 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://lists[.]wikimedia[.]org/mailman/listinfo/mediawiki-announce | strings |
| url | hxxps://www[.]mediawiki[.]org/wiki/Special:MyLanguage/Manual:Configuration_settings | strings |
| url | hxxps://www[.]mediawiki[.]org/wiki/Special:MyLanguage/Manual:FAQ | strings |
| hash | 4df6c9d7a1f11358ca58596708113ce171bd2cb4f044c5c528f9f3eb58744383 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
