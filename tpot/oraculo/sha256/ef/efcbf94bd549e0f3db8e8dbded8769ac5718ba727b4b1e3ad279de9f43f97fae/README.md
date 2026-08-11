# 🧬 Payload Analysis

`efcbf94bd549e0f3db8e8dbded8769ac5718ba727b4b1e3ad279de9f43f97fae`

## 📌 Resumen

Texto ASCII de 1.3 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `x86` en `hxxp://vitacocoyougoloco[.]potassium[.]st/x86`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/efcbf94bd549e0f3db8e8dbded8769ac5718ba727b4b1e3ad279de9f43f97fae.md](../../../../../malware-like/oraculo/downloader/efcbf94bd549e0f3db8e8dbded8769ac5718ba727b4b1e3ad279de9f43f97fae.md)


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
