# 🧬 Payload Analysis

`b0ebb2e8d682547a9c32e057382a7fc0316314046d2fb5269fa0ba14d384a995`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:52+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b0ebb2e8d682547a9c32e057382a7fc0316314046d2fb5269fa0ba14d384a995`
- **SHA1:** `12cf8454c76f7c45b0e4f7f06e3dc91a81bf244e`
- **MD5:** `39cd678ded2de342ba8f7b435b529faa`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 418 B |
| Entropía | 5.37 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 103.132.236.XXX | static_analysis |
| ip | 190.179.172.XXX | static_analysis |
| hash | b0ebb2e8d682547a9c32e057382a7fc0316314046d2fb5269fa0ba14d384a995 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
