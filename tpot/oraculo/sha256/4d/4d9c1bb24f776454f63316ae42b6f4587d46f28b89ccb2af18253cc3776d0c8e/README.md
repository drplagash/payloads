# 🧬 Payload Analysis

`4d9c1bb24f776454f63316ae42b6f4587d46f28b89ccb2af18253cc3776d0c8e`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:00:22+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4d9c1bb24f776454f63316ae42b6f4587d46f28b89ccb2af18253cc3776d0c8e`
- **SHA1:** `8fd36d99a1f788a8728ab56ff0a89212287fcbb1`
- **MD5:** `d5084d3cb15363067771200896f63322`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 447 B |
| Entropía | 5.2 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://docs[.]getodin[.]com/)@rhel9-app01:~$ | strings |
| hash | 4d9c1bb24f776454f63316ae42b6f4587d46f28b89ccb2af18253cc3776d0c8e | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
