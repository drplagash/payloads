# 🧬 Payload Analysis

`aebfd6e6b3f27575608ce6ddbd77e9b399fa3aeeafc40082a777ee0325764fa7`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:37:42+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `aebfd6e6b3f27575608ce6ddbd77e9b399fa3aeeafc40082a777ee0325764fa7`
- **SHA1:** `8fcbd0caa05259f60a9d0387ef4b84f0bbb93697`
- **MD5:** `cbbafc96cc359d6c67de13245741a81d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 102 B |
| Entropía | 5.08 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | aebfd6e6b3f27575608ce6ddbd77e9b399fa3aeeafc40082a777ee0325764fa7 | static_analysis |
| ip | 93.123.72.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
