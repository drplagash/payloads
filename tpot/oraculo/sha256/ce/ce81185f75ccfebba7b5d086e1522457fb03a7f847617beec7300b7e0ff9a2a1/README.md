# 🧬 Payload Analysis

`ce81185f75ccfebba7b5d086e1522457fb03a7f847617beec7300b7e0ff9a2a1`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:47+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ce81185f75ccfebba7b5d086e1522457fb03a7f847617beec7300b7e0ff9a2a1`
- **MD5:** `c20859a76483737075b25e4c7b1e881f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.24 |
| Strings | 14 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | [internal-ip-redacted] | static_analysis |
| url | hxxp://[internal-ip-redacted]:80/ | strings |
| url | hxxps://casper[.]ghost[.]org/v1.0.0/images/ghost-logo.svg | strings |
| url | hxxps://schema[.]org | strings |
| hash | ce81185f75ccfebba7b5d086e1522457fb03a7f847617beec7300b7e0ff9a2a1 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
