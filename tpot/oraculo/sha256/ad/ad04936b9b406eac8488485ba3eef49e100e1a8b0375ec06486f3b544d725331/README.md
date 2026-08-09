# 🧬 Payload Analysis

`ad04936b9b406eac8488485ba3eef49e100e1a8b0375ec06486f3b544d725331`

## 📌 Resumen

Artefacto de 548 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Status_404` en `hxxp://[internal-ip-redacted]/Status_404`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:29:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ad04936b9b406eac8488485ba3eef49e100e1a8b0375ec06486f3b544d725331`
- **SHA1:** `91e377e5706343634dcb28160216c9acd833e454`
- **MD5:** `a7ce9f30aebd3374024d2139e61eec38`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.37 |
| Strings | 12 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]/Status_404 | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | ad04936b9b406eac8488485ba3eef49e100e1a8b0375ec06486f3b544d725331 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
