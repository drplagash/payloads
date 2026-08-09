# 🧬 Payload Analysis

`e4a3a99ece4148bcfff0a74408b11b5d90aa56f4d52e5883d9807aed7567967c`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:49:32+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e4a3a99ece4148bcfff0a74408b11b5d90aa56f4d52e5883d9807aed7567967c`
- **SHA1:** `d3bfbe8ce6a027d53da9674e7ec5cdf0845a5f5b`
- **MD5:** `4e162f7dda8d7c8c276a7b3acb72d0d6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.32 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://www[.]mediawiki[.]org/wiki/Special:MyLanguage/Help:Contents | strings |
| hash | e4a3a99ece4148bcfff0a74408b11b5d90aa56f4d52e5883d9807aed7567967c | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
