# 🧬 Payload Analysis

`cec8cc319dc2d9b0eea3a62ead5935a160b1edefe06826d817f77e6207fabe34`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `fbml` en `hxxp://www[.]facebook[.]com/2008/fbml`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/cec8cc319dc2d9b0eea3a62ead5935a160b1edefe06826d817f77e6207fabe34.md](../../../../../malware-like/oraculo/downloader/cec8cc319dc2d9b0eea3a62ead5935a160b1edefe06826d817f77e6207fabe34.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:56.000000Z`
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
| url | hxxp://www[.]facebook[.]com/2008/fbml | strings |
| url | hxxp://opengraphprotocol[.]org/schema/ | strings |
| url | hxxp://www[.]w3[.]org/TR/xhtml1/DTD/xhtml1-transitional.dtd | strings |
| url | hxxp://www[.]w3[.]org/1999/xhtml | strings |
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
