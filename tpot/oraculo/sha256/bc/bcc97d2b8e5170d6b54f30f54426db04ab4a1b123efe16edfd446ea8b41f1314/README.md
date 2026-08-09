# 🧬 Payload Analysis

`bcc97d2b8e5170d6b54f30f54426db04ab4a1b123efe16edfd446ea8b41f1314`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `gg2` en `hxxp://2.26.124.XXX/gg2`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bcc97d2b8e5170d6b54f30f54426db04ab4a1b123efe16edfd446ea8b41f1314`
- **SHA1:** `619749adb78fe0708157302b7351a44fd5aa22eb`
- **MD5:** `33f1784bbe895ab49f6c75c4846eb86c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (696), with CRLF line terminators |
| Tamaño | 1.6 KiB |
| Entropía | 5.43 |
| Strings | 24 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Comunicación remota**
3. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (696), with CRLF line terminators; iocs=6

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://2.26.124.XXX/gg2 | strings |
| url | hxxp://2.26.124.XXX/gg2) | strings |
| ip | 94.154.43.XXX | static_analysis |
| ip | 2.26.124.XXX | static_analysis |
| ip | 190.179.140.XXX | static_analysis |
| hash | bcc97d2b8e5170d6b54f30f54426db04ab4a1b123efe16edfd446ea8b41f1314 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
