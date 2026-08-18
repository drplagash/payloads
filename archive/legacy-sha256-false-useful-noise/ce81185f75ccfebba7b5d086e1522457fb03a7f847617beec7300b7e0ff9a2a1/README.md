# 🧬 Payload Analysis

`ce81185f75ccfebba7b5d086e1522457fb03a7f847617beec7300b7e0ff9a2a1`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Infraestructura remota: `hxxps://schema[.]org`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/ce81185f75ccfebba7b5d086e1522457fb03a7f847617beec7300b7e0ff9a2a1.md](../../../../../malware-like/oraculo/downloader/ce81185f75ccfebba7b5d086e1522457fb03a7f847617beec7300b7e0ff9a2a1.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:47.000000Z`
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
| url | hxxps://schema[.]org | strings |
| url | hxxp://[internal-ip-redacted]:80/ | strings |
| url | hxxps://casper[.]ghost[.]org/v1.0.0/images/ghost-logo.svg | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | ce81185f75ccfebba7b5d086e1522457fb03a7f847617beec7300b7e0ff9a2a1 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
