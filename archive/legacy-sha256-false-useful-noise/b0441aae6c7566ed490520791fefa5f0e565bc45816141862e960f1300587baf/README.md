# 🧬 Payload Analysis

`b0441aae6c7566ed490520791fefa5f0e565bc45816141862e960f1300587baf`

## 📌 Resumen

Texto ASCII de 4.0 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `methodology` en `hxxps://umai[.]entelijan[.]com/methodology`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/b0441aae6c7566ed490520791fefa5f0e565bc45816141862e960f1300587baf.md](../../../../../malware-like/oraculo/downloader/b0441aae6c7566ed490520791fefa5f0e565bc45816141862e960f1300587baf.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b0441aae6c7566ed490520791fefa5f0e565bc45816141862e960f1300587baf`
- **SHA1:** `c593e3ee05fc1acee655a8f698cd48c3289e68b0`
- **MD5:** `52261e014e177ea260d49b28a764a071`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.06 |
| Strings | 124 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; strings=124; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://umai[.]entelijan[.]com/methodology) | strings |
| ip | 190.179.168.XXX | static_analysis |
| hash | b0441aae6c7566ed490520791fefa5f0e565bc45816141862e960f1300587baf | static_analysis |
| ip | 104.243.35.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
