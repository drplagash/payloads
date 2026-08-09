# 🧬 Payload Analysis

`b74509a410b60295ea7aa70206dae6019bd9fae3274ae6679a3c5ffa58a0d8b3`

## 📌 Resumen

Script JavaScript de 1.4 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `gg10` en `hxxp://94.154.43.XXX/gg10`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:31:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b74509a410b60295ea7aa70206dae6019bd9fae3274ae6679a3c5ffa58a0d8b3`
- **MD5:** `8fd4fa86d0190f50b81d40a1e794b037`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (555), with CRLF line terminators |
| Tamaño | 1.4 KiB |
| Entropía | 5.47 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (555), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/gg10) | strings |
| url | hxxp://94.154.43.XXX/gg10 | strings |
| ip | 94.154.43.XXX | static_analysis |
| ip | 190.179.164.XXX | static_analysis |
| hash | b74509a410b60295ea7aa70206dae6019bd9fae3274ae6679a3c5ffa58a0d8b3 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
