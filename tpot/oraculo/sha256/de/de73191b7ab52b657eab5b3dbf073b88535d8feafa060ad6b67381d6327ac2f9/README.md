# 🧬 Payload Analysis

`de73191b7ab52b657eab5b3dbf073b88535d8feafa060ad6b67381d6327ac2f9`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `de73191b7ab52b657eab5b3dbf073b88535d8feafa060ad6b67381d6327ac2f9`
- **SHA1:** `e970cbecf664b91f8b17dd6e94b8fb6bb09f4d25`
- **MD5:** `abc6083f0c072989874807c6c9d6b298`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.2 KiB |
| Entropía | 5.35 |
| Strings | 38 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 107.189.24.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | de73191b7ab52b657eab5b3dbf073b88535d8feafa060ad6b67381d6327ac2f9 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
