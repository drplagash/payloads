# 🧬 Payload Analysis

`c7c2d6caae5b98ca27944e064f5dc65565358b68e06dcffb847ac534bfc803bb`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c7c2d6caae5b98ca27944e064f5dc65565358b68e06dcffb847ac534bfc803bb`
- **SHA1:** `0d6994b12dffd0ad226ba419a342e5e4f87fc7ff`
- **MD5:** `9e9ed57716f914ec867f0ec73a40973d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 852 B |
| Entropía | 5.48 |
| Strings | 24 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 107.189.21.XXX | static_analysis |
| ip | 190.179.139.XXX | static_analysis |
| hash | c7c2d6caae5b98ca27944e064f5dc65565358b68e06dcffb847ac534bfc803bb | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
