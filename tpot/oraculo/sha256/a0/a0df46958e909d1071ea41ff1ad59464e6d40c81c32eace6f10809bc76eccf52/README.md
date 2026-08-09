# 🧬 Payload Analysis

`a0df46958e909d1071ea41ff1ad59464e6d40c81c32eace6f10809bc76eccf52`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:15:55+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a0df46958e909d1071ea41ff1ad59464e6d40c81c32eace6f10809bc76eccf52`
- **SHA1:** `06654c8d98d38bd0fcaf35968a5f8c4484b9321f`
- **MD5:** `10717f7dba69b2839cb1740ef89e86de`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 384 B |
| Entropía | 5.41 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 190.179.153.XXX | static_analysis |
| hash | a0df46958e909d1071ea41ff1ad59464e6d40c81c32eace6f10809bc76eccf52 | static_analysis |
| ip | 103.190.212.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
