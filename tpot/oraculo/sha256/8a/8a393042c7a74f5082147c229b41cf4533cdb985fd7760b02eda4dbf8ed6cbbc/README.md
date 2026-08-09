# 🧬 Payload Analysis

`8a393042c7a74f5082147c229b41cf4533cdb985fd7760b02eda4dbf8ed6cbbc`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:16+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8a393042c7a74f5082147c229b41cf4533cdb985fd7760b02eda4dbf8ed6cbbc`
- **SHA1:** `48b0d63620c6980aa70d57d566ed278d8392acbd`
- **MD5:** `367c102dedd23d6d82d2948062a5a710`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.0 KiB |
| Entropía | 5.45 |
| Strings | 33 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 107.189.26.XXX | static_analysis |
| ip | 190.179.140.XXX | static_analysis |
| hash | 8a393042c7a74f5082147c229b41cf4533cdb985fd7760b02eda4dbf8ed6cbbc | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
