# 🧬 Payload Analysis

`dd569f39d0d381ce22f2614803618bede1df8c83b4dd7e8f8cfa2edfa178a03a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:19+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dd569f39d0d381ce22f2614803618bede1df8c83b4dd7e8f8cfa2edfa178a03a`
- **SHA1:** `fec78426d1f5d936a5d02b16f4276722714170c7`
- **MD5:** `411927bd8f29e8afb8cac5e72a04259e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 801 B |
| Entropía | 5.5 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 104.37.127.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | dd569f39d0d381ce22f2614803618bede1df8c83b4dd7e8f8cfa2edfa178a03a | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
