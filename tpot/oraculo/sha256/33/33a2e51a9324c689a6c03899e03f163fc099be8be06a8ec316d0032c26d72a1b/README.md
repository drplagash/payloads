# 🧬 Payload Analysis

`33a2e51a9324c689a6c03899e03f163fc099be8be06a8ec316d0032c26d72a1b`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:58+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `33a2e51a9324c689a6c03899e03f163fc099be8be06a8ec316d0032c26d72a1b`
- **MD5:** `42afb3e43131521161e71caf61c73c43`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 624 B |
| Entropía | 5.39 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 152.239.122.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| hash | 33a2e51a9324c689a6c03899e03f163fc099be8be06a8ec316d0032c26d72a1b | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
