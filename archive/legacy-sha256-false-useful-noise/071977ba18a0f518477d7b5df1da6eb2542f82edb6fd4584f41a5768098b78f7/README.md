# 🧬 Payload Analysis

`071977ba18a0f518477d7b5df1da6eb2542f82edb6fd4584f41a5768098b78f7`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg10` en `hxxp://94.154.43.XXX/gg10`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/071977ba18a0f518477d7b5df1da6eb2542f82edb6fd4584f41a5768098b78f7.md](../../../../../malware-like/oraculo/downloader/071977ba18a0f518477d7b5df1da6eb2542f82edb6fd4584f41a5768098b78f7.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `071977ba18a0f518477d7b5df1da6eb2542f82edb6fd4584f41a5768098b78f7`
- **SHA1:** `55eb7a994cf5a4346d1fc309918f3e1e415b3116`
- **MD5:** `a70c30144b2b1b175f1433d421817440`

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
| ip | 190.179.139.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| hash | 071977ba18a0f518477d7b5df1da6eb2542f82edb6fd4584f41a5768098b78f7 | static_analysis |
| ip | 45.198.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
