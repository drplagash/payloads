# 🧬 Payload Analysis

`414241c7eb3bd683943b59eb35bbc5addfe50d28f48fb95c4de7a2818d6a0474`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `414241c7eb3bd683943b59eb35bbc5addfe50d28f48fb95c4de7a2818d6a0474`
- **SHA1:** `1c0216c765befdfb7e22cd2f1696c6aa4c209300`
- **MD5:** `3cc594356b29068d5ea408c28a789fe4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.0 KiB |
| Entropía | 5.44 |
| Strings | 33 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 172.86.119.XXX | static_analysis |
| ip | 190.179.140.XXX | static_analysis |
| hash | 414241c7eb3bd683943b59eb35bbc5addfe50d28f48fb95c4de7a2818d6a0474 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
