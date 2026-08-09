# 🧬 Payload Analysis

`e150728fbbfec0c12be08e44ac0f78d3468d87b73b9e9342ee0511863ac42b0b`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e150728fbbfec0c12be08e44ac0f78d3468d87b73b9e9342ee0511863ac42b0b`
- **SHA1:** `e750bd70885c532a2413fddc37f7be4f72f0effa`
- **MD5:** `c1b3967d00dd8eec74cbf1a85e5f13bb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | MPEG ADTS, AAC, v4 LTP, 16 kHz, surround |
| Tamaño | 1.4 KiB |
| Entropía | 7.87 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=MPEG ADTS, AAC, v4 LTP, 16 kHz, surround; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | e150728fbbfec0c12be08e44ac0f78d3468d87b73b9e9342ee0511863ac42b0b | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | media or resource |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
