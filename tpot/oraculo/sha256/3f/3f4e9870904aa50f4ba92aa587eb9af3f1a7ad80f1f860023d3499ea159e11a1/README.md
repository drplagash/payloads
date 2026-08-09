# 🧬 Payload Analysis

`3f4e9870904aa50f4ba92aa587eb9af3f1a7ad80f1f860023d3499ea159e11a1`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:36:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3f4e9870904aa50f4ba92aa587eb9af3f1a7ad80f1f860023d3499ea159e11a1`
- **MD5:** `42a94909d33c4456e9a855301ebfe623`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 938 B |
| Entropía | 5.62 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 134.0.0.XXX | static_analysis |
| ip | 190.179.174.XXX | static_analysis |
| hash | 3f4e9870904aa50f4ba92aa587eb9af3f1a7ad80f1f860023d3499ea159e11a1 | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
