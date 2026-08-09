# 🧬 Payload Analysis

`dfa1b65a3b02b8acf6a0c95d49fcb5b4c42a57aa989950aec09c730f4ffcaa99`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dfa1b65a3b02b8acf6a0c95d49fcb5b4c42a57aa989950aec09c730f4ffcaa99`
- **SHA1:** `14ffc61dff04ee0c94f14e4af4dfd089dacbed4c`
- **MD5:** `a9bfa5e830e059c2bb078ca77db7e9ae`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 396 B |
| Entropía | 5.38 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 135.0.0.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| hash | dfa1b65a3b02b8acf6a0c95d49fcb5b4c42a57aa989950aec09c730f4ffcaa99 | static_analysis |
| ip | 104.244.77.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
