# 🧬 Payload Analysis

`4d106f219c6ee2c6f239561539632b0fa3ee5a1fbbf68370a193a09f06d56cd9`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:10:07+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4d106f219c6ee2c6f239561539632b0fa3ee5a1fbbf68370a193a09f06d56cd9`
- **SHA1:** `aa251289b83c7c2b3e4c179c8ce86f76f2e57cdc`
- **MD5:** `26ef0aba8ece5a20c74849903b93ae15`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 403 B |
| Entropía | 5.37 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 117.55.202.XXX | static_analysis |
| ip | 190.179.166.XXX | static_analysis |
| hash | 4d106f219c6ee2c6f239561539632b0fa3ee5a1fbbf68370a193a09f06d56cd9 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
