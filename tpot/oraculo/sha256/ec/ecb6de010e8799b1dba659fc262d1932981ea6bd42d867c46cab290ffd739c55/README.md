# 🧬 Payload Analysis

`ecb6de010e8799b1dba659fc262d1932981ea6bd42d867c46cab290ffd739c55`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ecb6de010e8799b1dba659fc262d1932981ea6bd42d867c46cab290ffd739c55`
- **SHA1:** `7c18d363b950638f20497de5a20eae09af79e5f9`
- **MD5:** `0b6c7ef612cdc47842771a8abb7578ff`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 693 B |
| Entropía | 5.41 |
| Strings | 21 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.0.11.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | ecb6de010e8799b1dba659fc262d1932981ea6bd42d867c46cab290ffd739c55 | static_analysis |
| ip | 89.190.156.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
