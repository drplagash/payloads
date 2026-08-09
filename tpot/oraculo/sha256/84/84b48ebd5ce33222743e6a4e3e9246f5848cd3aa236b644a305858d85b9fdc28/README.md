# 🧬 Payload Analysis

`84b48ebd5ce33222743e6a4e3e9246f5848cd3aa236b644a305858d85b9fdc28`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:55+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `84b48ebd5ce33222743e6a4e3e9246f5848cd3aa236b644a305858d85b9fdc28`
- **SHA1:** `7d47b68015233da2674c67a95f28ad7ffd5c1ca7`
- **MD5:** `189bd8b22364c2960eb63b6abe5604c8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 738 B |
| Entropía | 5.34 |
| Strings | 22 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | 84b48ebd5ce33222743e6a4e3e9246f5848cd3aa236b644a305858d85b9fdc28 | static_analysis |
| ip | 87.106.206.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
