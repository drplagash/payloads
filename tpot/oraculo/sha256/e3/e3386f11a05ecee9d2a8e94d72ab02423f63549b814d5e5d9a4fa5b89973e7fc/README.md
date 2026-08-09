# 🧬 Payload Analysis

`e3386f11a05ecee9d2a8e94d72ab02423f63549b814d5e5d9a4fa5b89973e7fc`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `gg10` en `hxxp://94.154.43.XXX/gg10`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e3386f11a05ecee9d2a8e94d72ab02423f63549b814d5e5d9a4fa5b89973e7fc`
- **SHA1:** `6239631ef751edbd16390a9a8b7dbb637d7b31bf`
- **MD5:** `ea4683e7305ff56b294c435587285ff1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (698), with CRLF line terminators |
| Tamaño | 1.6 KiB |
| Entropía | 5.44 |
| Strings | 24 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (698), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/gg10 | strings |
| url | hxxp://94.154.43.XXX/gg10) | strings |
| ip | 94.154.43.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | e3386f11a05ecee9d2a8e94d72ab02423f63549b814d5e5d9a4fa5b89973e7fc | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
