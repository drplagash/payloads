# 🧬 Payload Analysis

`7da48a4e365b66d714e28d13b090c1fdb80b2446ad47f525e8cc46bfb2246955`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:05:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7da48a4e365b66d714e28d13b090c1fdb80b2446ad47f525e8cc46bfb2246955`
- **SHA1:** `3fc6c8bad6a8a0d21fe5ce9417e4b81a0398009a`
- **MD5:** `1acb6ba6b7d6efc7eb0d98674c5fb131`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 109 B |
| Entropía | 4.91 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 185.65.245.XXX | static_analysis |
| hash | 7da48a4e365b66d714e28d13b090c1fdb80b2446ad47f525e8cc46bfb2246955 | static_analysis |
| ip | 176.65.134.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
