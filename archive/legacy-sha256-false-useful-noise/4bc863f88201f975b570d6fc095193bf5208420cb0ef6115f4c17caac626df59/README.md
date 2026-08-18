# 🧬 Payload Analysis

`4bc863f88201f975b570d6fc095193bf5208420cb0ef6115f4c17caac626df59`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `11` en `hxxp://gmpg[.]org/xfn/11`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/4bc863f88201f975b570d6fc095193bf5208420cb0ef6115f4c17caac626df59.md](../../../../../malware-like/oraculo/downloader/4bc863f88201f975b570d6fc095193bf5208420cb0ef6115f4c17caac626df59.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4bc863f88201f975b570d6fc095193bf5208420cb0ef6115f4c17caac626df59`
- **SHA1:** `ffab92c743cbeec203e5b56c309330cb0fe67f0e`
- **MD5:** `6a9c24a8aa3c46b6ea6b29edfc1183b8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.78 |
| Strings | 12 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://gmpg[.]org/xfn/11 | strings |
| hash | 4bc863f88201f975b570d6fc095193bf5208420cb0ef6115f4c17caac626df59 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
