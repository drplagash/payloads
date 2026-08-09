# 🧬 Payload Analysis

`8e1d99189908265ea066f1149bcae898b93f46d3c013bf0bf1c998491812f677`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:37:42+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8e1d99189908265ea066f1149bcae898b93f46d3c013bf0bf1c998491812f677`
- **SHA1:** `8d39761e10c9e21c2406b4e5658095fbb26a35e9`
- **MD5:** `fba490dc4076ca908c77e6c5a4d7ce72`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 415 B |
| Entropía | 5.39 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 15.204.165.XXX | static_analysis |
| ip | 190.179.140.XXX | static_analysis |
| hash | 8e1d99189908265ea066f1149bcae898b93f46d3c013bf0bf1c998491812f677 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
