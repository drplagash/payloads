# 🧬 Payload Analysis

`318593a864b61c2f670682d3fd778eeffa3c49e17e4887e2d6ee40bdbae774fa`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `ghost-logo.svg` en `hxxps://casper[.]ghost[.]org/v1.0.0/images/ghost-logo.svg`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/318593a864b61c2f670682d3fd778eeffa3c49e17e4887e2d6ee40bdbae774fa.md](../../../../../malware-like/oraculo/downloader/318593a864b61c2f670682d3fd778eeffa3c49e17e4887e2d6ee40bdbae774fa.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:16:33.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `318593a864b61c2f670682d3fd778eeffa3c49e17e4887e2d6ee40bdbae774fa`
- **SHA1:** `dc4c68c116f492739002a1d1830352e923113798`
- **MD5:** `3fdf7891e96252be9e45aa1a65c3037f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.04 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=6

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://casper[.]ghost[.]org/v1.0.0/images/ghost-logo.svg | strings |
| url | hxxp://[internal-ip-redacted]:80/ | strings |
| url | hxxp://172[.]20[.]254[.] | strings |
| url | hxxps://casper[.]ghost[.]org/v1.0.0/images/blog-cover.jpg | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | 318593a864b61c2f670682d3fd778eeffa3c49e17e4887e2d6ee40bdbae774fa | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
