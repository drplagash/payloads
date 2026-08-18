# 🧬 Payload Analysis

`afbee1147296692d196bd859b856c52146a1bb7f23e98d9cecec541523ee273f`

## 📌 Resumen

Texto ASCII de 627 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `devprof` en `hxxp://schemas[.]xmlsoap[.]org/ws/2006/02/devprof`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/afbee1147296692d196bd859b856c52146a1bb7f23e98d9cecec541523ee273f.md](../../../../../malware-like/oraculo/downloader/afbee1147296692d196bd859b856c52146a1bb7f23e98d9cecec541523ee273f.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:06:23.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `afbee1147296692d196bd859b856c52146a1bb7f23e98d9cecec541523ee273f`
- **SHA1:** `99450d0ba059424b261244c8b124ca7c27456000`
- **MD5:** `07419a0e82685dbefff8ecba7f2b8ee0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (338) |
| Tamaño | 627 B |
| Entropía | 5.09 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (338); iocs=6

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2006/02/devprof | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2005/04/discovery | strings |
| url | hxxp://www[.]w3[.]org/2003/05/soap-envelope | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2005/04/discovery/Probe | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2004/08/addressing | strings |
| hash | afbee1147296692d196bd859b856c52146a1bb7f23e98d9cecec541523ee273f | static_analysis |
| ip | 146.88.241.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
