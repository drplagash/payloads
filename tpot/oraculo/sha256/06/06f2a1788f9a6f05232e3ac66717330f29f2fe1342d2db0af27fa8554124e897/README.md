# 🧬 Payload Analysis

`06f2a1788f9a6f05232e3ac66717330f29f2fe1342d2db0af27fa8554124e897`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:58:35+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `06f2a1788f9a6f05232e3ac66717330f29f2fe1342d2db0af27fa8554124e897`
- **SHA1:** `2d7bc1cd74ab5a7c552c9d5e1b0635bf6c062b08`
- **MD5:** `c5efbd91ff48f500a21392a7d094c4c4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 498 B |
| Entropía | 5.43 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://modat[.]io/)@db12-web01:~$ | strings |
| hash | 06f2a1788f9a6f05232e3ac66717330f29f2fe1342d2db0af27fa8554124e897 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
