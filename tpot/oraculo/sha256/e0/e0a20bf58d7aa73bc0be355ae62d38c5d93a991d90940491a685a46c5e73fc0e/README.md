# 🧬 Payload Analysis

`e0a20bf58d7aa73bc0be355ae62d38c5d93a991d90940491a685a46c5e73fc0e`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:55:58+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e0a20bf58d7aa73bc0be355ae62d38c5d93a991d90940491a685a46c5e73fc0e`
- **SHA1:** `0be9a27f221c8b2893eda4ced72611db9ca59627`
- **MD5:** `4c5f3965e513eade62a97e39defb182a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 411 B |
| Entropía | 5.42 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 15.204.165.XXX | static_analysis |
| ip | 190.179.144.XXX | static_analysis |
| hash | e0a20bf58d7aa73bc0be355ae62d38c5d93a991d90940491a685a46c5e73fc0e | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
