# 🧬 Payload Analysis

`daabd8690120f24727ecfb240e6614311b013040808e78cc40a1eebd22f934fc`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `daabd8690120f24727ecfb240e6614311b013040808e78cc40a1eebd22f934fc`
- **SHA1:** `a62d5cc241c373767ec38b7955c38049efc8fbaf`
- **MD5:** `3a2cd89e38702f4b2622267837734e8e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 795 B |
| Entropía | 5.52 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 163.39.184.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | daabd8690120f24727ecfb240e6614311b013040808e78cc40a1eebd22f934fc | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
