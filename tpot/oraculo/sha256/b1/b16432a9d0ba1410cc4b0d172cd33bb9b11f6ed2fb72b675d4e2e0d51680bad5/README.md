# 🧬 Payload Analysis

`b16432a9d0ba1410cc4b0d172cd33bb9b11f6ed2fb72b675d4e2e0d51680bad5`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `11` en `hxxp://gmpg[.]org/xfn/11`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/b16432a9d0ba1410cc4b0d172cd33bb9b11f6ed2fb72b675d4e2e0d51680bad5.md](../../../../../malware-like/oraculo/downloader/b16432a9d0ba1410cc4b0d172cd33bb9b11f6ed2fb72b675d4e2e0d51680bad5.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:15:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b16432a9d0ba1410cc4b0d172cd33bb9b11f6ed2fb72b675d4e2e0d51680bad5`
- **SHA1:** `ffdb3ba959e013c00f07c61cadcf6773472a0e9b`
- **MD5:** `b93fef73384602b060f258abf973d1ad`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.8 |
| Strings | 12 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://gmpg[.]org/xfn/11 | strings |
| hash | b16432a9d0ba1410cc4b0d172cd33bb9b11f6ed2fb72b675d4e2e0d51680bad5 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
