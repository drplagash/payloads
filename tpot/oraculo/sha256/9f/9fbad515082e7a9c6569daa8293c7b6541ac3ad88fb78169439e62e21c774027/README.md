# 🧬 Payload Analysis

`9fbad515082e7a9c6569daa8293c7b6541ac3ad88fb78169439e62e21c774027`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:27:00+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9fbad515082e7a9c6569daa8293c7b6541ac3ad88fb78169439e62e21c774027`
- **MD5:** `5581424fc91184c5a7f5abea7f9e0746`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (513), with no line terminators |
| Tamaño | 513 B |
| Entropía | 5.16 |
| Strings | 1 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2004/08/addressing | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2005/04/discovery | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2005/04/discovery/Probe | strings |
| url | hxxp://www[.]w3[.]org/2003/05/soap-envelope | strings |
| hash | 9fbad515082e7a9c6569daa8293c7b6541ac3ad88fb78169439e62e21c774027 | static_analysis |
| ip | 193.163.125.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
