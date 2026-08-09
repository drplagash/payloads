# 🧬 Payload Analysis

`a602ffa76b66e963f836f5ffa1f66f0403a15d306e7019f9accefa2dc1409108`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:40+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a602ffa76b66e963f836f5ffa1f66f0403a15d306e7019f9accefa2dc1409108`
- **SHA1:** `22e5a403a820c2bfb9a2135ec1e9979eb6e15a87`
- **MD5:** `f4e46c1544aba7576f35d151073cbbf9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 912 B |
| Entropía | 5.53 |
| Strings | 24 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 108.181.56.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| ip | 192.210.144.XXX | static_analysis |
| hash | a602ffa76b66e963f836f5ffa1f66f0403a15d306e7019f9accefa2dc1409108 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
