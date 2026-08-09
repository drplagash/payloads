# 🧬 Payload Analysis

`8d1e424490958f77b890523357df91142b4c223dc297fd510c97d4892e9c1857`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `gg10` en `hxxp://94.154.43.XXX/gg10`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:34:01.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8d1e424490958f77b890523357df91142b4c223dc297fd510c97d4892e9c1857`
- **MD5:** `34d599c090db1ea6269959ce13183152`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (698), with CRLF line terminators |
| Tamaño | 1.6 KiB |
| Entropía | 5.43 |
| Strings | 24 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (698), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/gg10 | strings |
| url | hxxp://94.154.43.XXX/gg10) | strings |
| ip | 190.179.164.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| hash | 8d1e424490958f77b890523357df91142b4c223dc297fd510c97d4892e9c1857 | static_analysis |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_Shell_Script |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
