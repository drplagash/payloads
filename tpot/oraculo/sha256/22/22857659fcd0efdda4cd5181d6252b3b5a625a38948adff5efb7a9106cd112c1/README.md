# 🧬 Payload Analysis

`22857659fcd0efdda4cd5181d6252b3b5a625a38948adff5efb7a9106cd112c1`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `22857659fcd0efdda4cd5181d6252b3b5a625a38948adff5efb7a9106cd112c1`
- **SHA1:** `fb2107b965040245da863b03db892534e1abc2b6`
- **MD5:** `10204711edf263f8a140c23dbe3a43a3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 411 B |
| Entropía | 5.41 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 190.179.140.XXX | static_analysis |
| ip | 72.251.5.XXX | static_analysis |
| hash | 22857659fcd0efdda4cd5181d6252b3b5a625a38948adff5efb7a9106cd112c1 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
