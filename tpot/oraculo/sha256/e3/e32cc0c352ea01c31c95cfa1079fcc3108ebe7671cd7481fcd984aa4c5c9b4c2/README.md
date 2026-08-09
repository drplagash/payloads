# 🧬 Payload Analysis

`e32cc0c352ea01c31c95cfa1079fcc3108ebe7671cd7481fcd984aa4c5c9b4c2`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:47:25+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e32cc0c352ea01c31c95cfa1079fcc3108ebe7671cd7481fcd984aa4c5c9b4c2`
- **SHA1:** `1715aee1bdb6f678cf94c93151cbae697444750f`
- **MD5:** `590c608a4bf193c1247057de3f01917e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (551), with CRLF line terminators |
| Tamaño | 864 B |
| Entropía | 5.59 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (551), with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 31.56.209.XXX | static_analysis |
| url | hxxp://31.56.209.XXX/x86;wget | strings |
| url | hxxp://vitacocoyougoloco[.]potassium[.]st/x86 | strings |
| hash | e32cc0c352ea01c31c95cfa1079fcc3108ebe7671cd7481fcd984aa4c5c9b4c2 | static_analysis |
| ip | 45.198.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
