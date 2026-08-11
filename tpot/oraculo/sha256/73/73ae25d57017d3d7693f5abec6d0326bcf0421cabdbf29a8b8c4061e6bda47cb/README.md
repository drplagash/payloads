# 🧬 Payload Analysis

`73ae25d57017d3d7693f5abec6d0326bcf0421cabdbf29a8b8c4061e6bda47cb`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Infraestructura remota: `hxxps://api[.]w[.]org/`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/73ae25d57017d3d7693f5abec6d0326bcf0421cabdbf29a8b8c4061e6bda47cb.md](../../../../../malware-like/oraculo/downloader/73ae25d57017d3d7693f5abec6d0326bcf0421cabdbf29a8b8c4061e6bda47cb.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:06:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `73ae25d57017d3d7693f5abec6d0326bcf0421cabdbf29a8b8c4061e6bda47cb`
- **SHA1:** `306ff7d603685667112c25144d626340ef77ae80`
- **MD5:** `5503f9f925370096691a24b3ed32e4f0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.4 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://api[.]w[.]org/ | strings |
| hash | 73ae25d57017d3d7693f5abec6d0326bcf0421cabdbf29a8b8c4061e6bda47cb | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
