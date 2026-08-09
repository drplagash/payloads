# 🧬 Payload Analysis

`aea510403c4caff24d7c44971a11da1542af18dc28fcaf6a88b4ffabb1e07167`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 120 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `index2.asp` en `hxxp://190.179.163.XXX:80/cgi-bin/index2.asp`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:46:43.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `aea510403c4caff24d7c44971a11da1542af18dc28fcaf6a88b4ffabb1e07167`
- **SHA1:** `0eb7dc4ac80c8fc48c1107c90baa51a12d1de850`
- **MD5:** `8ff284c2249bfcb312bace73136b5afb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 120 B |
| Entropía | 5.07 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://190.179.163.XXX:80/cgi-bin/index2.asp | strings |
| ip | 190.179.163.XXX | static_analysis |
| hash | aea510403c4caff24d7c44971a11da1542af18dc28fcaf6a88b4ffabb1e07167 | static_analysis |
| ip | 45.205.1.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
