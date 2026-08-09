# 🧬 Payload Analysis

`5846f2e9f0d2414b88118fbc7a03d2618e75224b0ed69fb326709cca12945092`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5846f2e9f0d2414b88118fbc7a03d2618e75224b0ed69fb326709cca12945092`
- **SHA1:** `26359111990486f593c4d13010cdc33fb6a3b159`
- **MD5:** `29b08c9c3362c89c010b2647c97202af`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.0 KiB |
| Entropía | 5.43 |
| Strings | 33 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 172.86.119.XXX | static_analysis |
| ip | 190.179.140.XXX | static_analysis |
| hash | 5846f2e9f0d2414b88118fbc7a03d2618e75224b0ed69fb326709cca12945092 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
