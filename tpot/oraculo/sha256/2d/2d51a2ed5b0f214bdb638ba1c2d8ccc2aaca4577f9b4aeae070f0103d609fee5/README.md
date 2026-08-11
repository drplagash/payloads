# 🧬 Payload Analysis

`2d51a2ed5b0f214bdb638ba1c2d8ccc2aaca4577f9b4aeae070f0103d609fee5`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg10` en `hxxp://94.154.43.XXX/gg10`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/2d51a2ed5b0f214bdb638ba1c2d8ccc2aaca4577f9b4aeae070f0103d609fee5.md](../../../../../malware-like/oraculo/downloader/2d51a2ed5b0f214bdb638ba1c2d8ccc2aaca4577f9b4aeae070f0103d609fee5.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:43:29.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2d51a2ed5b0f214bdb638ba1c2d8ccc2aaca4577f9b4aeae070f0103d609fee5`
- **MD5:** `28e410397668906cc900adefee157fd9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (698), with CRLF line terminators |
| Tamaño | 1.6 KiB |
| Entropía | 5.44 |
| Strings | 24 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/gg10 | strings |
| url | hxxp://94.154.43.XXX/gg10) | strings |
| ip | 190.179.167.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| hash | 2d51a2ed5b0f214bdb638ba1c2d8ccc2aaca4577f9b4aeae070f0103d609fee5 | static_analysis |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_Shell_Script |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
