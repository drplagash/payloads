# 🧬 Payload Analysis

`19611246df22be177dc47d60931e70aa3251a99cac515fcd48d57e145e0b0d8c`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `19611246df22be177dc47d60931e70aa3251a99cac515fcd48d57e145e0b0d8c`
- **SHA1:** `7f019c4d08096a77b8ca6a01773ca3b0cd01f63f`
- **MD5:** `aa67a3d09abfe57b29ca68450431b234`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.0 KiB |
| Entropía | 5.42 |
| Strings | 33 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 172.86.119.XXX | static_analysis |
| ip | 190.179.140.XXX | static_analysis |
| hash | 19611246df22be177dc47d60931e70aa3251a99cac515fcd48d57e145e0b0d8c | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
