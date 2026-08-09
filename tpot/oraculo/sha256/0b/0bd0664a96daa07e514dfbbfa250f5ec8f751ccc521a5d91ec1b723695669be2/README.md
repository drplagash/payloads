# 🧬 Payload Analysis

`0bd0664a96daa07e514dfbbfa250f5ec8f751ccc521a5d91ec1b723695669be2`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0bd0664a96daa07e514dfbbfa250f5ec8f751ccc521a5d91ec1b723695669be2`
- **SHA1:** `1c256a3656cc7bba4b572a99fa247bd3297adf3f`
- **MD5:** `500d7400feb249e70bddca34d7a910fa`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 864 B |
| Entropía | 5.56 |
| Strings | 24 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.139.XXX | static_analysis |
| ip | 216.126.224.XXX | static_analysis |
| hash | 0bd0664a96daa07e514dfbbfa250f5ec8f751ccc521a5d91ec1b723695669be2 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
