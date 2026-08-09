# 🧬 Payload Analysis

`cec8cc319dc2d9b0eea3a62ead5935a160b1edefe06826d817f77e6207fabe34`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:56+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cec8cc319dc2d9b0eea3a62ead5935a160b1edefe06826d817f77e6207fabe34`
- **SHA1:** `caf0737cad71db6f7afcd3bdc263b8ae9097cbff`
- **MD5:** `2a0c28e9036dfa4195b09e627ec64be4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.59 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://opengraphprotocol[.]org/schema/ | strings |
| url | hxxp://www[.]facebook[.]com/2008/fbml | strings |
| url | hxxp://www[.]w3[.]org/1999/xhtml | strings |
| url | hxxp://www[.]w3[.]org/TR/xhtml1/DTD/xhtml1-transitional.dtd | strings |
| hash | cec8cc319dc2d9b0eea3a62ead5935a160b1edefe06826d817f77e6207fabe34 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
