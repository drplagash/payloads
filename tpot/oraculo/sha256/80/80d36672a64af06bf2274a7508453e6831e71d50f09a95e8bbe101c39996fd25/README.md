# 🧬 Payload Analysis

`80d36672a64af06bf2274a7508453e6831e71d50f09a95e8bbe101c39996fd25`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `80d36672a64af06bf2274a7508453e6831e71d50f09a95e8bbe101c39996fd25`
- **SHA1:** `bb71fd0b209aeab8c8c4901d7d0a2fabe4e9bdd5`
- **MD5:** `b2d2ca019c8bd5080cc9be008110e9c7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 403 B |
| Entropía | 5.33 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 190.179.139.XXX | static_analysis |
| ip | 51.68.34.XXX | static_analysis |
| hash | 80d36672a64af06bf2274a7508453e6831e71d50f09a95e8bbe101c39996fd25 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
