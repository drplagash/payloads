# 🧬 Payload Analysis

`6597fca728cc2a8a9a6d8e98bfcea6144dfb885c0e3022957b4b8ee746b6bf93`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (856), with CRLF line terminators de 1.0 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `rondo` en `hxxp://45.153.34.XXX/rondo`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:25.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6597fca728cc2a8a9a6d8e98bfcea6144dfb885c0e3022957b4b8ee746b6bf93`
- **MD5:** `04509884106e4ef384ead745209768eb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (856), with CRLF line terminators |
| Tamaño | 1.0 KiB |
| Entropía | 5.47 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (856), with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://45.153.34.XXX/rondo. | strings |
| ip | 190.179.175.XXX | static_analysis |
| ip | 45.153.34.XXX | static_analysis |
| hash | 6597fca728cc2a8a9a6d8e98bfcea6144dfb885c0e3022957b4b8ee746b6bf93 | static_analysis |
| ip | 94.154.43.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
