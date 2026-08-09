# 🧬 Payload Analysis

`b731bf6f282901f8c9c392e01a41c880a16dc2ebd562720099c0fb1a95ff5a62`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:20+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b731bf6f282901f8c9c392e01a41c880a16dc2ebd562720099c0fb1a95ff5a62`
- **MD5:** `9beb20296448d50f0799418e1af86347`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 548 B |
| Entropía | 5.38 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.175.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| hash | b731bf6f282901f8c9c392e01a41c880a16dc2ebd562720099c0fb1a95ff5a62 | static_analysis |
| ip | 141.98.11.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
