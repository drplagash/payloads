# 🧬 Payload Analysis

`3ed9c71ac3b05bf1f2f3a50a9049a97269f6d62f5a9ddae202c02e114ab23bf8`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (480), with CRLF line terminators de 1.2 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `x86` en `hxxp://217.60.195.XXX:8080/x86`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:41:09.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3ed9c71ac3b05bf1f2f3a50a9049a97269f6d62f5a9ddae202c02e114ab23bf8`
- **SHA1:** `557bf01f0b5cc66fcc52b7509725d2631e59e241`
- **MD5:** `c08b1e411a1d78e836180efcb626eff9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (480), with CRLF line terminators |
| Tamaño | 1.2 KiB |
| Entropía | 5.76 |
| Strings | 18 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (480), with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://217.60.195.XXX:8080/x86; | strings |
| ip | 190.179.166.XXX | static_analysis |
| ip | 217.60.195.XXX | static_analysis |
| hash | 3ed9c71ac3b05bf1f2f3a50a9049a97269f6d62f5a9ddae202c02e114ab23bf8 | static_analysis |
| ip | 45.198.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
