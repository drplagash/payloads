# 🧬 Payload Analysis

`67e6436732479c353f032c966935de67ed1f9a7b555d7ec2b4e8e97b53bba28a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `67e6436732479c353f032c966935de67ed1f9a7b555d7ec2b4e8e97b53bba28a`
- **SHA1:** `23fce82bc21a51b74bf7cc8009a9df386816a74e`
- **MD5:** `dbae77c4f80582bc6726350c94d65fba`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.51 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 147.46.216.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 67e6436732479c353f032c966935de67ed1f9a7b555d7ec2b4e8e97b53bba28a | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
