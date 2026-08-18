# 🧬 Payload Analysis

`6333805b756ac12bf18ac1c38f299ebb535821fe146c4cee9e5e0783ba3592de`

## 📌 Resumen

Script JavaScript de 1.4 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg10` en `hxxp://94.154.43.XXX/gg10`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/6333805b756ac12bf18ac1c38f299ebb535821fe146c4cee9e5e0783ba3592de.md](../../../../../malware-like/oraculo/downloader/6333805b756ac12bf18ac1c38f299ebb535821fe146c4cee9e5e0783ba3592de.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:44:08.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6333805b756ac12bf18ac1c38f299ebb535821fe146c4cee9e5e0783ba3592de`
- **MD5:** `08e8021dd1019f7cf1fad8d9929ad620`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (555), with CRLF line terminators |
| Tamaño | 1.4 KiB |
| Entropía | 5.47 |
| Strings | 23 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/gg10 | strings |
| url | hxxp://94.154.43.XXX/gg10) | strings |
| ip | 190.179.167.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| hash | 6333805b756ac12bf18ac1c38f299ebb535821fe146c4cee9e5e0783ba3592de | static_analysis |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_Shell_Script |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
