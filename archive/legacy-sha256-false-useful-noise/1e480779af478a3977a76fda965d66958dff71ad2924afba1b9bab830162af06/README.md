# 🧬 Payload Analysis

`1e480779af478a3977a76fda965d66958dff71ad2924afba1b9bab830162af06`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `svg` en `hxxp://www[.]w3[.]org/2000/svg`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/1e480779af478a3977a76fda965d66958dff71ad2924afba1b9bab830162af06.md](../../../../../malware-like/oraculo/downloader/1e480779af478a3977a76fda965d66958dff71ad2924afba1b9bab830162af06.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1e480779af478a3977a76fda965d66958dff71ad2924afba1b9bab830162af06`
- **SHA1:** `77507c8fdf8d16d6a0efbb5af83ef7015d20a519`
- **MD5:** `037ddecaaa6097b794642a87100c6e11`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.35 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]w3[.]org/2000/svg | strings |
| url | hxxp://www[.]w3[.]org/1999/xlink | strings |
| hash | 1e480779af478a3977a76fda965d66958dff71ad2924afba1b9bab830162af06 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
