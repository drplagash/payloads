# 🧬 Payload Analysis

`44319664008d1a272b74a781ae5a61a352932ad40a77445ef06c3481915d5674`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `44319664008d1a272b74a781ae5a61a352932ad40a77445ef06c3481915d5674`
- **SHA1:** `8848b6e99a406cfe93c3cef3642dc2c7bf658c9e`
- **MD5:** `f26aa495603958ba2dd7819f0d87a38d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 364 B |
| Entropía | 5.23 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 172.110.223.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| ip | 34.80.0.XXX | static_analysis |
| hash | 44319664008d1a272b74a781ae5a61a352932ad40a77445ef06c3481915d5674 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
