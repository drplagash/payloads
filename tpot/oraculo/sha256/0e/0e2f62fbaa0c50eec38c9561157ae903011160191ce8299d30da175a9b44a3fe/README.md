# 🧬 Payload Analysis

`0e2f62fbaa0c50eec38c9561157ae903011160191ce8299d30da175a9b44a3fe`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:44:48.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0e2f62fbaa0c50eec38c9561157ae903011160191ce8299d30da175a9b44a3fe`
- **MD5:** `a7b75f5fc669ce40582d345d3881fbe7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.1 KiB |
| Entropía | 4.92 |
| Strings | 30 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 179.43.167.XXX | static_analysis |
| ip | 190.179.164.XXX | static_analysis |
| hash | 0e2f62fbaa0c50eec38c9561157ae903011160191ce8299d30da175a9b44a3fe | static_analysis |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers5 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
