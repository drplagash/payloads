# 🧬 Payload Analysis

`65bdc1562820de7f2102be2a3271e43a3cc01777fb3188217872aca4ff4fc125`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg10` en `hxxp://94.154.43.XXX/gg10`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/65bdc1562820de7f2102be2a3271e43a3cc01777fb3188217872aca4ff4fc125.md](../../../../../malware-like/oraculo/downloader/65bdc1562820de7f2102be2a3271e43a3cc01777fb3188217872aca4ff4fc125.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:57:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `65bdc1562820de7f2102be2a3271e43a3cc01777fb3188217872aca4ff4fc125`
- **SHA1:** `20dc2a4269ea33e4974ba2ab28606298a909eda4`
- **MD5:** `2df096f06c3a74e4a69490d7c207ffc8`

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
| ip | 190.179.168.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| hash | 65bdc1562820de7f2102be2a3271e43a3cc01777fb3188217872aca4ff4fc125 | static_analysis |
| ip | 45.198.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
