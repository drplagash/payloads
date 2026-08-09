# 🧬 Payload Analysis

`42dc84a53c89aaa1fe841931659ccc23e2c9d7f5a6e787a3905fe64152cb3b29`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:00:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `42dc84a53c89aaa1fe841931659ccc23e2c9d7f5a6e787a3905fe64152cb3b29`
- **SHA1:** `8268bc6ba247375fcea7cc38456c63902ca4d254`
- **MD5:** `b0b81132c0ad6c95579b9c0bf4648037`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 414 B |
| Entropía | 5.41 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 162.217.103.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 42dc84a53c89aaa1fe841931659ccc23e2c9d7f5a6e787a3905fe64152cb3b29 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
