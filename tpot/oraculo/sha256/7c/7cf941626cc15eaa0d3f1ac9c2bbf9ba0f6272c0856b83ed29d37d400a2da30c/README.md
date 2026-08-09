# 🧬 Payload Analysis

`7cf941626cc15eaa0d3f1ac9c2bbf9ba0f6272c0856b83ed29d37d400a2da30c`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:20+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7cf941626cc15eaa0d3f1ac9c2bbf9ba0f6272c0856b83ed29d37d400a2da30c`
- **MD5:** `4ff9613c3a271a922aa2d0c0edd33d5f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 683 B |
| Entropía | 5.41 |
| Strings | 21 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.175.XXX | static_analysis |
| hash | 7cf941626cc15eaa0d3f1ac9c2bbf9ba0f6272c0856b83ed29d37d400a2da30c | static_analysis |
| ip | 89.190.156.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
