# 🧬 Payload Analysis

`bd667b359a231ace9369a98d7ba4e66f9ce52c24226544e255a738fa35e859e1`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:09:22+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bd667b359a231ace9369a98d7ba4e66f9ce52c24226544e255a738fa35e859e1`
- **SHA1:** `77a9964f426a76ad4619ef93343201e322c47169`
- **MD5:** `d8f235daa96b5a5b4e9f16ccb3ae24f9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 268 B |
| Entropía | 5.29 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.166.XXX | static_analysis |
| hash | bd667b359a231ace9369a98d7ba4e66f9ce52c24226544e255a738fa35e859e1 | static_analysis |
| ip | 107.175.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
