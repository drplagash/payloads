# 🧬 Payload Analysis

`49f8c4862fbbbb2a5d940764ada1bc8f6287813e89758176677759bf64c8ee12`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:58:10+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `49f8c4862fbbbb2a5d940764ada1bc8f6287813e89758176677759bf64c8ee12`
- **SHA1:** `7d1aa99e340a433a1a38d79d45cf5c7ae0fa7a6c`
- **MD5:** `e4382cbfb0563e73219cb412b46242ca`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 415 B |
| Entropía | 5.4 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 15.204.165.XXX | static_analysis |
| ip | 190.179.130.XXX | static_analysis |
| hash | 49f8c4862fbbbb2a5d940764ada1bc8f6287813e89758176677759bf64c8ee12 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
