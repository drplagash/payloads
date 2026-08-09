# 🧬 Payload Analysis

`e214bcd76d58c77ab68682d0636a3062ef64fd53beba00a5ce8cc1b6c06b60c0`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e214bcd76d58c77ab68682d0636a3062ef64fd53beba00a5ce8cc1b6c06b60c0`
- **SHA1:** `cc94f8162bc4959d1c88ab4d338afb01fab4bacc`
- **MD5:** `9cff498e0c887f050efb4be6947b3987`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 805 B |
| Entropía | 5.49 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 185.146.246.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | e214bcd76d58c77ab68682d0636a3062ef64fd53beba00a5ce8cc1b6c06b60c0 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
