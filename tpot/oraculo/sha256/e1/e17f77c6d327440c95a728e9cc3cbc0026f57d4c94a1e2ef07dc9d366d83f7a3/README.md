# 🧬 Payload Analysis

`e17f77c6d327440c95a728e9cc3cbc0026f57d4c94a1e2ef07dc9d366d83f7a3`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:20:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e17f77c6d327440c95a728e9cc3cbc0026f57d4c94a1e2ef07dc9d366d83f7a3`
- **SHA1:** `c7f950a1f7de0d167135c60d957959b8e06ff79b`
- **MD5:** `54cea268718a06828cb014abd343d5b6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (775), with CRLF line terminators |
| Tamaño | 916 B |
| Entropía | 5.35 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (775), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 109.104.153.XXX | static_analysis |
| url | hxxp://109.104.153.XXX/icy.sh | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| hash | e17f77c6d327440c95a728e9cc3cbc0026f57d4c94a1e2ef07dc9d366d83f7a3 | static_analysis |
| ip | 103.96.140.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
