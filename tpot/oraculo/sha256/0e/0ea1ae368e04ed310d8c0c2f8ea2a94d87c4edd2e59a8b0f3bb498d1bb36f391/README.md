# 🧬 Payload Analysis

`0ea1ae368e04ed310d8c0c2f8ea2a94d87c4edd2e59a8b0f3bb498d1bb36f391`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:10+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0ea1ae368e04ed310d8c0c2f8ea2a94d87c4edd2e59a8b0f3bb498d1bb36f391`
- **SHA1:** `5c06b7c353414eb3999108a354894f09239c1638`
- **MD5:** `7ecef0a2f005f052a0c415dc46d66364`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.2 KiB |
| Entropía | 5.37 |
| Strings | 38 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 107.189.24.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 0ea1ae368e04ed310d8c0c2f8ea2a94d87c4edd2e59a8b0f3bb498d1bb36f391 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
