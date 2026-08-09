# 🧬 Payload Analysis

`7703c6c014d706c02d5098ad4bddd9619b6e7c801e7814e9a7c1bd7424fd57f0`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:31:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7703c6c014d706c02d5098ad4bddd9619b6e7c801e7814e9a7c1bd7424fd57f0`
- **SHA1:** `3d43380c5fa8d2710f8607fe776e66025c0d46b5`
- **MD5:** `5c99177dceab149664fedef616cbacb1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 738 B |
| Entropía | 5.35 |
| Strings | 22 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | 7703c6c014d706c02d5098ad4bddd9619b6e7c801e7814e9a7c1bd7424fd57f0 | static_analysis |
| ip | 87.106.223.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
