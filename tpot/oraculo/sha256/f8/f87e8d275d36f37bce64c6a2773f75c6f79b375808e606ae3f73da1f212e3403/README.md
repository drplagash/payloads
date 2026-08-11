# 🧬 Payload Analysis

`f87e8d275d36f37bce64c6a2773f75c6f79b375808e606ae3f73da1f212e3403`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg10` en `hxxp://94.154.43.XXX/gg10`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/f87e8d275d36f37bce64c6a2773f75c6f79b375808e606ae3f73da1f212e3403.md](../../../../../malware-like/oraculo/downloader/f87e8d275d36f37bce64c6a2773f75c6f79b375808e606ae3f73da1f212e3403.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f87e8d275d36f37bce64c6a2773f75c6f79b375808e606ae3f73da1f212e3403`
- **MD5:** `c3996574b4dd5f79b8911bd5e63d0ada`

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
| ip | 190.179.175.XXX | static_analysis |
| hash | f87e8d275d36f37bce64c6a2773f75c6f79b375808e606ae3f73da1f212e3403 | static_analysis |
| ip | 45.198.224.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
