# 🧬 Payload Analysis

`9561851b99273a769a5bc01376a056660d5c9cf1b921832b97d42739dd1b862d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:25+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9561851b99273a769a5bc01376a056660d5c9cf1b921832b97d42739dd1b862d`
- **MD5:** `f5d0567fb75ad90a4e609aa2e3d0941e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 797 B |
| Entropía | 5.49 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 188.167.81.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| hash | 9561851b99273a769a5bc01376a056660d5c9cf1b921832b97d42739dd1b862d | static_analysis |
| ip | 144.172.106.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
