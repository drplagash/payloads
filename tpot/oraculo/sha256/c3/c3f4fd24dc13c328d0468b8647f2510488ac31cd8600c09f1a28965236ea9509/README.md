# 🧬 Payload Analysis

`c3f4fd24dc13c328d0468b8647f2510488ac31cd8600c09f1a28965236ea9509`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (677), with CRLF line terminators de 992 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `cumshotnews` en `hxxp://192.142.28.XXX/cumshotnews`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c3f4fd24dc13c328d0468b8647f2510488ac31cd8600c09f1a28965236ea9509`
- **SHA1:** `309d1d4df814325ba4b821dc7113e99dbeb2b5cc`
- **MD5:** `3b0cfc2c22668c1b45a571407dc09f42`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (677), with CRLF line terminators |
| Tamaño | 992 B |
| Entropía | 5.52 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (677), with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://192.142.28.XXX/cumshotnews; | strings |
| ip | 192.142.28.XXX | static_analysis |
| hash | c3f4fd24dc13c328d0468b8647f2510488ac31cd8600c09f1a28965236ea9509 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
