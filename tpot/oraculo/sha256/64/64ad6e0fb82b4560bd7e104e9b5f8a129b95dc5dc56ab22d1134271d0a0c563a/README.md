# 🧬 Payload Analysis

`64ad6e0fb82b4560bd7e104e9b5f8a129b95dc5dc56ab22d1134271d0a0c563a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `64ad6e0fb82b4560bd7e104e9b5f8a129b95dc5dc56ab22d1134271d0a0c563a`
- **SHA1:** `7ffc274cfd913b2b13a24aea51861130d582a38a`
- **MD5:** `9b4f5ef097c9428dd4a6b9c0e1579915`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 797 B |
| Entropía | 5.51 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 172.5.230.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 64ad6e0fb82b4560bd7e104e9b5f8a129b95dc5dc56ab22d1134271d0a0c563a | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
