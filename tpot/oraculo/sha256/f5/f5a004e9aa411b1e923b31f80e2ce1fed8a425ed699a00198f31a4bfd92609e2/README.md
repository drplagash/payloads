# 🧬 Payload Analysis

`f5a004e9aa411b1e923b31f80e2ce1fed8a425ed699a00198f31a4bfd92609e2`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (856), with CRLF line terminators de 1.0 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `rondo` en `hxxp://45.153.34.XXX/rondo`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:19.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f5a004e9aa411b1e923b31f80e2ce1fed8a425ed699a00198f31a4bfd92609e2`
- **SHA1:** `eaa097e62d105b94a2dc7410589f201e2d495813`
- **MD5:** `2aeda2a93782272df74ec0d0fc392a84`

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
| ip | 45.153.34.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | f5a004e9aa411b1e923b31f80e2ce1fed8a425ed699a00198f31a4bfd92609e2 | static_analysis |
| ip | 94.154.43.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
