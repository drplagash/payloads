# 🧬 Payload Analysis

`5fd9c2163884218e0c486e5373b42391bfd2f4631de5a34614b0c48b7c6de0eb`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5fd9c2163884218e0c486e5373b42391bfd2f4631de5a34614b0c48b7c6de0eb`
- **SHA1:** `31b732c4310644a41f82bfa401817a6e523ec137`
- **MD5:** `59e8e777a6543ac9897713f4485ce55c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 949 B |
| Entropía | 5.53 |
| Strings | 29 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 160.119.71.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 5fd9c2163884218e0c486e5373b42391bfd2f4631de5a34614b0c48b7c6de0eb | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
