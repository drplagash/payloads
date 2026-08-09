# 🧬 Payload Analysis

`b080c69a9a86bd384f36b1746e9e7ff237aa1734ac420835cbbbef81d26187f9`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b080c69a9a86bd384f36b1746e9e7ff237aa1734ac420835cbbbef81d26187f9`
- **SHA1:** `87121ba11b44c20ae2590ad42df47f89f907a2f4`
- **MD5:** `ecc82ee4b353d5fec4ed8ff9eafdcddd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.49 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 141.183.120.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | b080c69a9a86bd384f36b1746e9e7ff237aa1734ac420835cbbbef81d26187f9 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
