# 🧬 Payload Analysis

`a67b52784bc7981a79314727c5ca97d1c2bd51f984bd1651a3e5bcfe9d0aa272`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 113 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `json` en `hxxp://ip-api[.]com/json/`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:58:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a67b52784bc7981a79314727c5ca97d1c2bd51f984bd1651a3e5bcfe9d0aa272`
- **SHA1:** `4c2566bf9fa86da0b1bb406715144a101482a91d`
- **MD5:** `7449540c77601ac01b60ca973b80ec02`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 113 B |
| Entropía | 4.73 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://ip-api[.]com/json/ | strings |
| hash | a67b52784bc7981a79314727c5ca97d1c2bd51f984bd1651a3e5bcfe9d0aa272 | static_analysis |
| ip | 204.76.203.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
