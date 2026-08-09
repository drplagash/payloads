# 🧬 Payload Analysis

`a6ba9aca659ce7050fb1faf49e17d212aef7ef6c42c0bcabd537ddee911f5d28`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a6ba9aca659ce7050fb1faf49e17d212aef7ef6c42c0bcabd537ddee911f5d28`
- **SHA1:** `fc8aa38106a62600d776980658f595d60321f344`
- **MD5:** `4c80f7b0b0c47c171b20859f1eac75d2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 793 B |
| Entropía | 5.55 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 129.6.215.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | a6ba9aca659ce7050fb1faf49e17d212aef7ef6c42c0bcabd537ddee911f5d28 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
