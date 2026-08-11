# 🧬 Payload Analysis

`872e5761e5bebda2199ee9a5002fcf9189349dc79441803dbb5dee1c68f65839`

## 📌 Resumen

Script JavaScript de 1.4 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg10` en `hxxp://94.154.43.XXX/gg10`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/872e5761e5bebda2199ee9a5002fcf9189349dc79441803dbb5dee1c68f65839.md](../../../../../malware-like/oraculo/downloader/872e5761e5bebda2199ee9a5002fcf9189349dc79441803dbb5dee1c68f65839.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:31:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `872e5761e5bebda2199ee9a5002fcf9189349dc79441803dbb5dee1c68f65839`
- **MD5:** `492446a380e5dc918666098aa4821d2e`

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
| url | hxxp://94.154.43.XXX/gg10) | strings |
| url | hxxp://94.154.43.XXX/gg10 | strings |
| ip | 94.154.43.XXX | static_analysis |
| ip | 190.179.164.XXX | static_analysis |
| hash | 872e5761e5bebda2199ee9a5002fcf9189349dc79441803dbb5dee1c68f65839 | static_analysis |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_Shell_Script |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
