# 🧬 Payload Analysis

`36f50077f2719a1bbc2064c1c5de1292475c722775a542ac34ddd4dfeb138504`

## 📌 Resumen

Artefacto identificado como XML 1.0 document, ASCII text, with very long lines (513), with no line terminators de 513 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Probe` en `hxxp://schemas[.]xmlsoap[.]org/ws/2005/04/discovery/Probe`. Se extrajeron 4 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `36f50077f2719a1bbc2064c1c5de1292475c722775a542ac34ddd4dfeb138504`
- **SHA1:** `5cfb71648f95a3fb741d92587378992810836427`
- **MD5:** `bd3bccf9fa93767e05327875c8e9a1a0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (513), with no line terminators |
| Tamaño | 513 B |
| Entropía | 5.17 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (513), with no line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2005/04/discovery/Probe | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2005/04/discovery | strings |
| url | hxxp://www[.]w3[.]org/2003/05/soap-envelope | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2004/08/addressing | strings |
| hash | 36f50077f2719a1bbc2064c1c5de1292475c722775a542ac34ddd4dfeb138504 | static_analysis |
| ip | 193.163.125.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
