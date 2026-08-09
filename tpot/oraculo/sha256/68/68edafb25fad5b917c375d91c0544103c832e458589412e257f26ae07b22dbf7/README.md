# 🧬 Payload Analysis

`68edafb25fad5b917c375d91c0544103c832e458589412e257f26ae07b22dbf7`

## 📌 Resumen

Artefacto de 548 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Status_404` en `hxxp://[internal-ip-redacted]/Status_404`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:26:56.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `68edafb25fad5b917c375d91c0544103c832e458589412e257f26ae07b22dbf7`
- **SHA1:** `bac38a50ef6e8ebfc10bd7546c86a45b59e8f69a`
- **MD5:** `849c9baeeab80e97dc7df819302c8543`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.36 |
| Strings | 12 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]/Status_404 | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | 68edafb25fad5b917c375d91c0544103c832e458589412e257f26ae07b22dbf7 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
