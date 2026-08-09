# 🧬 Payload Analysis

`268aa4104af30ac21eba362cde105174336ce5c09faab4c34b404dda3d500adc`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:41:51+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `268aa4104af30ac21eba362cde105174336ce5c09faab4c34b404dda3d500adc`
- **SHA1:** `faf26e90d176b6d27fd5285883ab4e12a6a4c0cb`
- **MD5:** `78b7e9866caa361ffec93c0cf9bf9c7b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 712 B |
| Entropía | 5.51 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.166.XXX | static_analysis |
| ip | 217.154.196.XXX | static_analysis |
| hash | 268aa4104af30ac21eba362cde105174336ce5c09faab4c34b404dda3d500adc | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
