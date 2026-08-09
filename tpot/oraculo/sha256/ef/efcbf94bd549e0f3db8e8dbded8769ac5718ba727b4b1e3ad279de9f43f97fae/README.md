# 🧬 Payload Analysis

`efcbf94bd549e0f3db8e8dbded8769ac5718ba727b4b1e3ad279de9f43f97fae`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (551), with CRLF line terminators de 1.3 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `x86` en `hxxp://vitacocoyougoloco[.]potassium[.]st/x86`. Se extrajeron 2 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:47:25.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `efcbf94bd549e0f3db8e8dbded8769ac5718ba727b4b1e3ad279de9f43f97fae`
- **SHA1:** `39b24c0d6fb6bcf04779cc2332ef385bbcc08c9f`
- **MD5:** `7d3522bc74708941802261b40c501346`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (551), with CRLF line terminators |
| Tamaño | 1.3 KiB |
| Entropía | 5.72 |
| Strings | 18 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (551), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://vitacocoyougoloco[.]potassium[.]st/x86 | strings |
| url | hxxp://31.56.209.XXX/x86;wget | strings |
| ip | 190.179.144.XXX | static_analysis |
| ip | 31.56.209.XXX | static_analysis |
| hash | efcbf94bd549e0f3db8e8dbded8769ac5718ba727b4b1e3ad279de9f43f97fae | static_analysis |
| ip | 45.198.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
