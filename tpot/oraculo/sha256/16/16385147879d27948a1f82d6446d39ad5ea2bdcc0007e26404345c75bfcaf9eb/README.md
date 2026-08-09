# 🧬 Payload Analysis

`16385147879d27948a1f82d6446d39ad5ea2bdcc0007e26404345c75bfcaf9eb`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:55:00+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `16385147879d27948a1f82d6446d39ad5ea2bdcc0007e26404345c75bfcaf9eb`
- **SHA1:** `264be114663ae091a224c2f3f74124f16aa32658`
- **MD5:** `60dc8fb691fec556f94a4078dbf2430f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 131 B |
| Entropía | 4.98 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| hash | 16385147879d27948a1f82d6446d39ad5ea2bdcc0007e26404345c75bfcaf9eb | static_analysis |
| ip | 175.210.184.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
