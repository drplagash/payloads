# 🧬 Payload Analysis

`cf961a92876b1a5bb04b239208ec7545a2bfe08fd27c4aa166c0ed600b065786`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cf961a92876b1a5bb04b239208ec7545a2bfe08fd27c4aa166c0ed600b065786`
- **SHA1:** `5bc0b590a0f5e901b2072b34d999afb9137d44f7`
- **MD5:** `77233edd94ea8a8c2c26a247d8f8c97e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | old Microsoft 8086 x.out relocatable |
| Tamaño | 21 B |
| Entropía | 3.92 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=old Microsoft 8086 x.out relocatable; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | cf961a92876b1a5bb04b239208ec7545a2bfe08fd27c4aa166c0ed600b065786 | static_analysis |
| ip | 146.88.241.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
