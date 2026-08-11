# 🧬 Payload Analysis

`340fa7f141a6e09b614edc53aa4b05fdccd70f378de06dc34e6fc17292d2bf00`

## 📌 Resumen

Script JavaScript de 1.4 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg10` en `hxxp://94.154.43.XXX/gg10`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/340fa7f141a6e09b614edc53aa4b05fdccd70f378de06dc34e6fc17292d2bf00.md](../../../../../malware-like/oraculo/downloader/340fa7f141a6e09b614edc53aa4b05fdccd70f378de06dc34e6fc17292d2bf00.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `340fa7f141a6e09b614edc53aa4b05fdccd70f378de06dc34e6fc17292d2bf00`
- **MD5:** `e08170c57520072b66c670f365f48883`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (555), with CRLF line terminators |
| Tamaño | 1.4 KiB |
| Entropía | 5.47 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (555), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/gg10 | strings |
| url | hxxp://94.154.43.XXX/gg10) | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| hash | 340fa7f141a6e09b614edc53aa4b05fdccd70f378de06dc34e6fc17292d2bf00 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
