# 🧬 Payload Analysis

`31c6601ce0e1553f6b60f97b47e27a2580c3b8bff4de0b7d8d658c2c76e0059d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:44:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `31c6601ce0e1553f6b60f97b47e27a2580c3b8bff4de0b7d8d658c2c76e0059d`
- **MD5:** `2f0df2825a16b6363ef803562e8bccaa`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 992 B |
| Entropía | 5.69 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | 31c6601ce0e1553f6b60f97b47e27a2580c3b8bff4de0b7d8d658c2c76e0059d | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
