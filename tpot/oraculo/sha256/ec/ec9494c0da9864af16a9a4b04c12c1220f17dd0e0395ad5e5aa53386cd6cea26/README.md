# 🧬 Payload Analysis

`ec9494c0da9864af16a9a4b04c12c1220f17dd0e0395ad5e5aa53386cd6cea26`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:19+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ec9494c0da9864af16a9a4b04c12c1220f17dd0e0395ad5e5aa53386cd6cea26`
- **SHA1:** `8a840effa128b0816ae6d9161b39eec28afc1e56`
- **MD5:** `b79bd2454afe7f5e0dc0fce9e3ba9ed1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 805 B |
| Entropía | 5.48 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 130.188.123.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | ec9494c0da9864af16a9a4b04c12c1220f17dd0e0395ad5e5aa53386cd6cea26 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
