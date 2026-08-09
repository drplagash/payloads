# 🧬 Payload Analysis

`8dc385f94e01dcf7cbffb0e777ce128fde7f6e4ada0858cdd6d3895979177be0`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8dc385f94e01dcf7cbffb0e777ce128fde7f6e4ada0858cdd6d3895979177be0`
- **SHA1:** `9c6d5b79e319941ad5b292725e71a73ae6e0637b`
- **MD5:** `8a3d90a5b53514d0a4886326cb50351b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 801 B |
| Entropía | 5.49 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 175.204.109.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 8dc385f94e01dcf7cbffb0e777ce128fde7f6e4ada0858cdd6d3895979177be0 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
