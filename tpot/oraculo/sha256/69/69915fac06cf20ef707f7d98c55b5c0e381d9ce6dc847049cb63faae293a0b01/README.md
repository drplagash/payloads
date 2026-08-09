# 🧬 Payload Analysis

`69915fac06cf20ef707f7d98c55b5c0e381d9ce6dc847049cb63faae293a0b01`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `69915fac06cf20ef707f7d98c55b5c0e381d9ce6dc847049cb63faae293a0b01`
- **SHA1:** `4ac95133d7e442efd36dde0c91707887d73daf00`
- **MD5:** `1484304831f6be431d13d8e64ab9a085`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 797 B |
| Entropía | 5.48 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 115.16.204.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 69915fac06cf20ef707f7d98c55b5c0e381d9ce6dc847049cb63faae293a0b01 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
