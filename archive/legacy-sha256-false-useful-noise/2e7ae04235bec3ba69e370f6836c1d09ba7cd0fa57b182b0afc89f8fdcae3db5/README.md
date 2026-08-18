# 🧬 Payload Analysis

`2e7ae04235bec3ba69e370f6836c1d09ba7cd0fa57b182b0afc89f8fdcae3db5`

## 📌 Resumen

Texto ASCII de 866 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `adb.sh` en `hxxp://196.251.121.XXX/a3f8d2/adb.sh`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/2e7ae04235bec3ba69e370f6836c1d09ba7cd0fa57b182b0afc89f8fdcae3db5.md](../../../../../malware-like/oraculo/downloader/2e7ae04235bec3ba69e370f6836c1d09ba7cd0fa57b182b0afc89f8fdcae3db5.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:58:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2e7ae04235bec3ba69e370f6836c1d09ba7cd0fa57b182b0afc89f8fdcae3db5`
- **SHA1:** `36cb31081651308b0c281656042315c814fc49e5`
- **MD5:** `c01c4b40c3e689e020022d2d776150bf`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (712), with CRLF line terminators |
| Tamaño | 866 B |
| Entropía | 5.34 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (712), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://196.251.121.XXX/a3f8d2/adb.sh; | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| ip | 196.251.121.XXX | static_analysis |
| hash | 2e7ae04235bec3ba69e370f6836c1d09ba7cd0fa57b182b0afc89f8fdcae3db5 | static_analysis |
| ip | 115.84.178.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
