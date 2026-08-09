# 🧬 Payload Analysis

`ba51ef8d0cd1cb226e2f83acc2aea6ca092dd5144d54ba92fbe3d510418f5617`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ba51ef8d0cd1cb226e2f83acc2aea6ca092dd5144d54ba92fbe3d510418f5617`
- **SHA1:** `b7e603b12e60824fa513b94a64dc01992b34ec8e`
- **MD5:** `26600220f4b515c5644513762ccbfc6b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.5 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 185.61.180.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | ba51ef8d0cd1cb226e2f83acc2aea6ca092dd5144d54ba92fbe3d510418f5617 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
