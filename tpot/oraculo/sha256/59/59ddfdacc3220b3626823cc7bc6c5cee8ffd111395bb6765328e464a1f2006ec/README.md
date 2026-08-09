# 🧬 Payload Analysis

`59ddfdacc3220b3626823cc7bc6c5cee8ffd111395bb6765328e464a1f2006ec`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `59ddfdacc3220b3626823cc7bc6c5cee8ffd111395bb6765328e464a1f2006ec`
- **SHA1:** `305ef4964c791c6fcb883df09f3d6d7879e09975`
- **MD5:** `5c8ecc7e0596cacfaa7b1f4ef20b17ff`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 117 B |
| Entropía | 5.09 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| hash | 59ddfdacc3220b3626823cc7bc6c5cee8ffd111395bb6765328e464a1f2006ec | static_analysis |
| ip | 185.93.89.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
