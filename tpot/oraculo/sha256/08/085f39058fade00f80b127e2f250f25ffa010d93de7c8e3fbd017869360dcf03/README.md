# 🧬 Payload Analysis

`085f39058fade00f80b127e2f250f25ffa010d93de7c8e3fbd017869360dcf03`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 124 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `index2.asp` en `hxxp://190.179.166.XXX:80/cgi-bin/index2.asp`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:10:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `085f39058fade00f80b127e2f250f25ffa010d93de7c8e3fbd017869360dcf03`
- **SHA1:** `7f99eb9265fea25f68215bf8ab66862296d58b1e`
- **MD5:** `0e1ad92685d93ce0b1da81a79b0d27c7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 124 B |
| Entropía | 5.09 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://190.179.166.XXX:80/cgi-bin/index2.asp | strings |
| ip | 190.179.166.XXX | static_analysis |
| hash | 085f39058fade00f80b127e2f250f25ffa010d93de7c8e3fbd017869360dcf03 | static_analysis |
| ip | 45.205.1.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
