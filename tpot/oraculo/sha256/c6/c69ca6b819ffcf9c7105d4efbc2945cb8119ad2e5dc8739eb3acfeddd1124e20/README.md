# 🧬 Payload Analysis

`c69ca6b819ffcf9c7105d4efbc2945cb8119ad2e5dc8739eb3acfeddd1124e20`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c69ca6b819ffcf9c7105d4efbc2945cb8119ad2e5dc8739eb3acfeddd1124e20`
- **SHA1:** `d5508a74d73c3b3bf33425307e0a152b04f55734`
- **MD5:** `ac9d80ca199bac9f805b51060f59cd38`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.1 KiB |
| Entropía | 5.4 |
| Strings | 36 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 107.189.21.XXX | static_analysis |
| ip | 190.179.139.XXX | static_analysis |
| hash | c69ca6b819ffcf9c7105d4efbc2945cb8119ad2e5dc8739eb3acfeddd1124e20 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
