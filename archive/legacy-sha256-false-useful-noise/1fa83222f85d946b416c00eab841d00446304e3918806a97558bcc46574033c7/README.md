# 🧬 Payload Analysis

`1fa83222f85d946b416c00eab841d00446304e3918806a97558bcc46574033c7`

## 📌 Resumen

Texto ASCII de 4.0 KiB. La evidencia disponible identifica capacidad de descarga remota. Infraestructura remota: `hxxps://umai[.]entelijan[.]co`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/1fa83222f85d946b416c00eab841d00446304e3918806a97558bcc46574033c7.md](../../../../../malware-like/oraculo/downloader/1fa83222f85d946b416c00eab841d00446304e3918806a97558bcc46574033c7.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1fa83222f85d946b416c00eab841d00446304e3918806a97558bcc46574033c7`
- **SHA1:** `148163fde5c18ae361218f4ff7997a354804ce9a`
- **MD5:** `617a18b1284fa73d0d6709682371bca7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.06 |
| Strings | 124 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; strings=124; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://umai[.]entelijan[.]co | strings |
| url | hxxps://umai[.]entelijan[.]com/methodology) | strings |
| ip | 190.179.168.XXX | static_analysis |
| hash | 1fa83222f85d946b416c00eab841d00446304e3918806a97558bcc46574033c7 | static_analysis |
| ip | 104.243.35.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
