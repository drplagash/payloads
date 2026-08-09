# 🧬 Payload Analysis

`66b2debb6ce02d73570f727cadd2606f07e60be453a6a827db1c030b3475e5a3`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `66b2debb6ce02d73570f727cadd2606f07e60be453a6a827db1c030b3475e5a3`
- **SHA1:** `4eb2d09a0c5f84d493ca843785dc25f1105de99b`
- **MD5:** `57c086869d34c100d18820caa31aa49a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 803 B |
| Entropía | 5.46 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 119.109.213.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 66b2debb6ce02d73570f727cadd2606f07e60be453a6a827db1c030b3475e5a3 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
