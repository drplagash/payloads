# 🧬 Payload Analysis

`b31e1c2913f4c94006f89ba30ed1ff81e0f7c00360cf0e987c6928e7ad2f5cd0`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `fbml` en `hxxp://www[.]facebook[.]com/2008/fbml`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/b31e1c2913f4c94006f89ba30ed1ff81e0f7c00360cf0e987c6928e7ad2f5cd0.md](../../../../../malware-like/oraculo/downloader/b31e1c2913f4c94006f89ba30ed1ff81e0f7c00360cf0e987c6928e7ad2f5cd0.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:22:20.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b31e1c2913f4c94006f89ba30ed1ff81e0f7c00360cf0e987c6928e7ad2f5cd0`
- **SHA1:** `849e13bd44e332150815414de2e83a341c37e841`
- **MD5:** `3ba07c1b542e3641303f85f248f6c321`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.62 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]facebook[.]com/2008/fbml | strings |
| url | hxxp://www[.]w3[.]org/TR/xhtml1/DTD/xhtml1-transitional.dtd | strings |
| url | hxxp://opengraphprotocol[.]org/schema/ | strings |
| url | hxxp://www[.]w3[.]org/1999/xhtml | strings |
| hash | b31e1c2913f4c94006f89ba30ed1ff81e0f7c00360cf0e987c6928e7ad2f5cd0 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
