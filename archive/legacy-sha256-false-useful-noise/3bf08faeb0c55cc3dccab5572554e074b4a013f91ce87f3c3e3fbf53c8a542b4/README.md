# 🧬 Payload Analysis

`3bf08faeb0c55cc3dccab5572554e074b4a013f91ce87f3c3e3fbf53c8a542b4`

## 📌 Resumen

Script JavaScript de 1.3 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg2` en `hxxp://94.154.43.XXX/gg2`. **C2 / infraestructura de control:**

- **Posible C2:** `94.154.43.XXX` — confianza Alto, evidencia hardcoded_in_payload Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/3bf08faeb0c55cc3dccab5572554e074b4a013f91ce87f3c3e3fbf53c8a542b4.md](../../../../../malware-like/oraculo/downloader/3bf08faeb0c55cc3dccab5572554e074b4a013f91ce87f3c3e3fbf53c8a542b4.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3bf08faeb0c55cc3dccab5572554e074b4a013f91ce87f3c3e3fbf53c8a542b4`
- **SHA1:** `d20244edc725acb367af1c721b8176cec74b515d`
- **MD5:** `000946641808706247bce802c61d3632`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (696), with CRLF line terminators |
| Tamaño | 1.3 KiB |
| Entropía | 5.35 |
| Strings | 15 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Comunicación remota**
3. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (696), with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/gg2) | strings |
| url | hxxp://94.154.43.XXX/gg2 | strings |
| ip | 94.154.43.XXX | static_analysis |
| hash | 3bf08faeb0c55cc3dccab5572554e074b4a013f91ce87f3c3e3fbf53c8a542b4 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
