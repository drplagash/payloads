# 🧬 Payload Analysis

`a022782c8d81cd6b51351a5f23ea934854b74bf820858ad26b2802e2f826db06`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Comunicación remota, Cambio de permisos.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a022782c8d81cd6b51351a5f23ea934854b74bf820858ad26b2802e2f826db06`
- **SHA1:** `e533c9bf22bde4fdbd139efb402b302c435ae552`
- **MD5:** `8057187cd704d98d3fb088d4e7441147`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (682), with CRLF line terminators |
| Tamaño | 1.3 KiB |
| Entropía | 5.34 |
| Strings | 15 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Comunicación remota**
3. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (682), with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 2.26.124.XXX | static_analysis |
| url | hxxp://2.26.124.XXX:99/gg | strings |
| url | hxxp://2.26.124.XXX:99/gg) | strings |
| hash | a022782c8d81cd6b51351a5f23ea934854b74bf820858ad26b2802e2f826db06 | static_analysis |
| ip | 94.154.43.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
