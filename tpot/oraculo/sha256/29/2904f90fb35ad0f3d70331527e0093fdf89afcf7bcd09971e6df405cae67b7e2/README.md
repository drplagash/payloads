# 🧬 Payload Analysis

`2904f90fb35ad0f3d70331527e0093fdf89afcf7bcd09971e6df405cae67b7e2`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2904f90fb35ad0f3d70331527e0093fdf89afcf7bcd09971e6df405cae67b7e2`
- **SHA1:** `10a8c6e94a14758bd42f517bf4c3fb23a9ad1662`
- **MD5:** `3aa4183ee3fef109d724479a0a7f6014`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.51 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 107.161.34.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 2904f90fb35ad0f3d70331527e0093fdf89afcf7bcd09971e6df405cae67b7e2 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
