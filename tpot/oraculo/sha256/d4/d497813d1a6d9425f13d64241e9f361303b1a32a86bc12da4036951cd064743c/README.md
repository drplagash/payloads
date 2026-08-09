# 🧬 Payload Analysis

`d497813d1a6d9425f13d64241e9f361303b1a32a86bc12da4036951cd064743c`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:11:29+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d497813d1a6d9425f13d64241e9f361303b1a32a86bc12da4036951cd064743c`
- **SHA1:** `0484b73d10b58592728f8c7e0b445b17176a8ee7`
- **MD5:** `6375be567b5b8fdb3af1ee0825912763`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 44 B |
| Entropía | 4.27 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | d497813d1a6d9425f13d64241e9f361303b1a32a86bc12da4036951cd064743c | static_analysis |
| ip | 45.90.163.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
