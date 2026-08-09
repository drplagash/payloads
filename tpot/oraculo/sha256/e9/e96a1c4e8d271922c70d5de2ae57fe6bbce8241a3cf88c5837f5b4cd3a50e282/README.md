# 🧬 Payload Analysis

`e96a1c4e8d271922c70d5de2ae57fe6bbce8241a3cf88c5837f5b4cd3a50e282`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e96a1c4e8d271922c70d5de2ae57fe6bbce8241a3cf88c5837f5b4cd3a50e282`
- **SHA1:** `f31f77b0869bf7588b33ff4c546653f140a9e6f3`
- **MD5:** `ca6ed293025a94250e14d45aee6f9c92`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 795 B |
| Entropía | 5.51 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 26.221.90.XXX | static_analysis |
| hash | e96a1c4e8d271922c70d5de2ae57fe6bbce8241a3cf88c5837f5b4cd3a50e282 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
