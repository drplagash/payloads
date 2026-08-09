# 🧬 Payload Analysis

`d35f6d991c47166255b140dd72be7db29605fd1184cc1a3a53a7ce307c2e46c2`

## 📌 Resumen

Artefacto de 548 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `11` en `hxxp://gmpg[.]org/xfn/11`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:40:04.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d35f6d991c47166255b140dd72be7db29605fd1184cc1a3a53a7ce307c2e46c2`
- **MD5:** `47e9285a2ea7d27cb5a66f5b3409b528`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.77 |
| Strings | 13 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://gmpg[.]org/xfn/11 | strings |
| hash | d35f6d991c47166255b140dd72be7db29605fd1184cc1a3a53a7ce307c2e46c2 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
