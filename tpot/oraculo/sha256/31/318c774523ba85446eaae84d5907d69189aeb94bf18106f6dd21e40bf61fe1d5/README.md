# 🧬 Payload Analysis

`318c774523ba85446eaae84d5907d69189aeb94bf18106f6dd21e40bf61fe1d5`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:22:21+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `318c774523ba85446eaae84d5907d69189aeb94bf18106f6dd21e40bf61fe1d5`
- **SHA1:** `10decdeb8a8e209af45352826169c9b6c289daeb`
- **MD5:** `92ef993ad5e0b8a9aa3e5449f20d86e1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 467 B |
| Entropía | 5.2 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://modat[.]io/)@fedora-edge:~$ | strings |
| hash | 318c774523ba85446eaae84d5907d69189aeb94bf18106f6dd21e40bf61fe1d5 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
