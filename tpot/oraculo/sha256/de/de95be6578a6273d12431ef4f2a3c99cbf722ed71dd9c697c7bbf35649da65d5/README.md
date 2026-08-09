# 🧬 Payload Analysis

`de95be6578a6273d12431ef4f2a3c99cbf722ed71dd9c697c7bbf35649da65d5`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:31:17+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `de95be6578a6273d12431ef4f2a3c99cbf722ed71dd9c697c7bbf35649da65d5`
- **MD5:** `51cbf74822abd880c6368b91443201dd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (403), with CRLF line terminators |
| Tamaño | 1003 B |
| Entropía | 5.52 |
| Strings | 16 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (403), with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.164.XXX | static_analysis |
| ip | 45.153.34.XXX | static_analysis |
| hash | de95be6578a6273d12431ef4f2a3c99cbf722ed71dd9c697c7bbf35649da65d5 | static_analysis |
| ip | 94.154.43.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
