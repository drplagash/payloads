# 🧬 Payload Analysis

`78fb1ccb6058a28da9aa40f4d58e56f46d10394ffb04e09ae9a2fccb5a5b94b6`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg10` en `hxxp://94.154.43.XXX/gg10`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/78fb1ccb6058a28da9aa40f4d58e56f46d10394ffb04e09ae9a2fccb5a5b94b6.md](../../../../../malware-like/oraculo/downloader/78fb1ccb6058a28da9aa40f4d58e56f46d10394ffb04e09ae9a2fccb5a5b94b6.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:57:22.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `78fb1ccb6058a28da9aa40f4d58e56f46d10394ffb04e09ae9a2fccb5a5b94b6`
- **SHA1:** `3c049849868670184e6b533a17294e7422cb2d9d`
- **MD5:** `767b6401ae73716ee72b33bafb2dc55e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (698), with CRLF line terminators |
| Tamaño | 1.6 KiB |
| Entropía | 5.43 |
| Strings | 24 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (698), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/gg10) | strings |
| url | hxxp://94.154.43.XXX/gg10 | strings |
| ip | 94.154.43.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| hash | 78fb1ccb6058a28da9aa40f4d58e56f46d10394ffb04e09ae9a2fccb5a5b94b6 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
