# 🧬 Payload Analysis

`564219b40480a9f77804f55ab20b7090ff839d9db2284bc7c70bab33fd7a8201`

## 📌 Resumen

Script JavaScript de 1.3 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg10` en `hxxp://94.154.43.XXX/gg10`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/564219b40480a9f77804f55ab20b7090ff839d9db2284bc7c70bab33fd7a8201.md](../../../../../malware-like/oraculo/downloader/564219b40480a9f77804f55ab20b7090ff839d9db2284bc7c70bab33fd7a8201.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:57:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `564219b40480a9f77804f55ab20b7090ff839d9db2284bc7c70bab33fd7a8201`
- **SHA1:** `3429eccad70dfc84cb8508bb80f4c08f19625135`
- **MD5:** `85b0ac3861893956b34963c3c3339b9a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (698), with CRLF line terminators |
| Tamaño | 1.3 KiB |
| Entropía | 5.36 |
| Strings | 15 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (698), with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/gg10 | strings |
| url | hxxp://94.154.43.XXX/gg10) | strings |
| ip | 94.154.43.XXX | static_analysis |
| hash | 564219b40480a9f77804f55ab20b7090ff839d9db2284bc7c70bab33fd7a8201 | static_analysis |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_Shell_Script |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
