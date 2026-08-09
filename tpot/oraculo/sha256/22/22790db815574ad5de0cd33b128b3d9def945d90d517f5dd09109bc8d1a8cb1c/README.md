# 🧬 Payload Analysis

`22790db815574ad5de0cd33b128b3d9def945d90d517f5dd09109bc8d1a8cb1c`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:34:01+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `22790db815574ad5de0cd33b128b3d9def945d90d517f5dd09109bc8d1a8cb1c`
- **MD5:** `76d677edcbd215a11adba6f3bff7f019`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 723 B |
| Entropía | 5.56 |
| Strings | 20 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | [internal-ip-redacted] | static_analysis |
| ip | 190.179.164.XXX | static_analysis |
| hash | 22790db815574ad5de0cd33b128b3d9def945d90d517f5dd09109bc8d1a8cb1c | static_analysis |
| ip | 23.94.184.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
