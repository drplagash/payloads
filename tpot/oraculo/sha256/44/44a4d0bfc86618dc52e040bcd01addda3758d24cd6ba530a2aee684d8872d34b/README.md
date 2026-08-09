# 🧬 Payload Analysis

`44a4d0bfc86618dc52e040bcd01addda3758d24cd6ba530a2aee684d8872d34b`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:08:37+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `44a4d0bfc86618dc52e040bcd01addda3758d24cd6ba530a2aee684d8872d34b`
- **SHA1:** `a3ee17b7e4542af6df4e15d1e7afbf25b28c209a`
- **MD5:** `afe1da9b634e858c4409f066f9f52133`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 30 B |
| Entropía | 3.87 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 44a4d0bfc86618dc52e040bcd01addda3758d24cd6ba530a2aee684d8872d34b | static_analysis |
| ip | 107.175.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
