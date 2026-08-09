# 🧬 Payload Analysis

`222a09ebb802acc2afc4ddfd6113e1808831a2df1835b762cd875132180a21c6`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 124 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `index2.asp` en `hxxp://190.179.128.XXX:80/cgi-bin/index2.asp`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:21:42.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `222a09ebb802acc2afc4ddfd6113e1808831a2df1835b762cd875132180a21c6`
- **SHA1:** `38fd126a43f369d7a33562e4976c97d3ee6adb37`
- **MD5:** `ef2958be80a558ad22d74f49c149cbce`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 124 B |
| Entropía | 5.02 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://190.179.128.XXX:80/cgi-bin/index2.asp | strings |
| ip | 190.179.128.XXX | static_analysis |
| hash | 222a09ebb802acc2afc4ddfd6113e1808831a2df1835b762cd875132180a21c6 | static_analysis |
| ip | 45.205.1.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
