# 🧬 Payload Analysis

`ec536224f6af31101846498e1940b41a0d4be55e47575c722bd0015a7592d005`

## 📌 Resumen

Script JavaScript de 1.2 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `gg2` en `hxxp://94.154.43.XXX/gg2`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ec536224f6af31101846498e1940b41a0d4be55e47575c722bd0015a7592d005`
- **SHA1:** `7077aed6b675ce079e157e046bd690a21c0add7c`
- **MD5:** `963c06033a0243c3c952d309123ca1fc`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (554), with CRLF line terminators |
| Tamaño | 1.2 KiB |
| Entropía | 5.39 |
| Strings | 14 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (554), with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/gg2) | strings |
| url | hxxp://94.154.43.XXX/gg2 | strings |
| ip | 94.154.43.XXX | static_analysis |
| hash | ec536224f6af31101846498e1940b41a0d4be55e47575c722bd0015a7592d005 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
