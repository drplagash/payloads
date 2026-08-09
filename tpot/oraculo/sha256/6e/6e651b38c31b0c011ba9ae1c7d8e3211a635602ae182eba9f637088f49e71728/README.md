# 🧬 Payload Analysis

`6e651b38c31b0c011ba9ae1c7d8e3211a635602ae182eba9f637088f49e71728`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:18:27+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6e651b38c31b0c011ba9ae1c7d8e3211a635602ae182eba9f637088f49e71728`
- **SHA1:** `e4ae56ae7f2eb6defbf436184f013829498d5ff1`
- **MD5:** `d40141cf84271f0e64d2be9df7f97eba`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (710), with CRLF line terminators |
| Tamaño | 864 B |
| Entropía | 5.33 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (710), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 83.142.209.XXX | static_analysis |
| url | hxxp://83.142.209.XXX/a3f8d2/adb.sh; | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| hash | 6e651b38c31b0c011ba9ae1c7d8e3211a635602ae182eba9f637088f49e71728 | static_analysis |
| ip | 177.22.44.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
