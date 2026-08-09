# 🧬 Payload Analysis

`687573a0621f9517f139bd5e0ddad9dd4ac0305dacf9e01afc2e0ca75ed70e34`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:55:35+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `687573a0621f9517f139bd5e0ddad9dd4ac0305dacf9e01afc2e0ca75ed70e34`
- **SHA1:** `922189a1d7003ae1899e1227789af03a6405d2a0`
- **MD5:** `978ae0e9c55f5509448fcb8323bf4828`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 192 B |
| Entropía | 4.95 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://docs-cortex[.]paloaltonetworks[.]com/r/1/Cortex-Xpanse/Scanning-activity | strings |
| hash | 687573a0621f9517f139bd5e0ddad9dd4ac0305dacf9e01afc2e0ca75ed70e34 | static_analysis |
| ip | 198.235.24.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
