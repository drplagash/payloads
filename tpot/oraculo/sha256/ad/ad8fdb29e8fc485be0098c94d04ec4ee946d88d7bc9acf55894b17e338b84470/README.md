# 🧬 Payload Analysis

`ad8fdb29e8fc485be0098c94d04ec4ee946d88d7bc9acf55894b17e338b84470`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ad8fdb29e8fc485be0098c94d04ec4ee946d88d7bc9acf55894b17e338b84470`
- **SHA1:** `687c1df9e8c595de655ff6e793cf47762ecd7e70`
- **MD5:** `bfc9ffe57cb350a2d693882a205c026e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.51 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 184.73.187.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | ad8fdb29e8fc485be0098c94d04ec4ee946d88d7bc9acf55894b17e338b84470 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
