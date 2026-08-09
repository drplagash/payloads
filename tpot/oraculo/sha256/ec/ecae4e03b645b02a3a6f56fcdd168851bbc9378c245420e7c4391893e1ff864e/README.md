# 🧬 Payload Analysis

`ecae4e03b645b02a3a6f56fcdd168851bbc9378c245420e7c4391893e1ff864e`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ecae4e03b645b02a3a6f56fcdd168851bbc9378c245420e7c4391893e1ff864e`
- **SHA1:** `35bde451f3a41d536ca53c2ee683ed7b82b5d0a9`
- **MD5:** `b156c7cb5eea06d8b641e59a4cac4352`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 412 B |
| Entropía | 5.37 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 172.110.223.XXX | static_analysis |
| ip | 190.179.139.XXX | static_analysis |
| hash | ecae4e03b645b02a3a6f56fcdd168851bbc9378c245420e7c4391893e1ff864e | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
