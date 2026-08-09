# 🧬 Payload Analysis

`7bb75a987e57da40a949c42554ca476d8124dca6a7492cbfc801f7df3dc01d5f`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7bb75a987e57da40a949c42554ca476d8124dca6a7492cbfc801f7df3dc01d5f`
- **SHA1:** `7bc0690010fa56155c8896b4c7ff1097c5d23db4`
- **MD5:** `d61f67e5d95f6c362fc5e0610e6ebee0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 55 B |
| Entropía | 4.72 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 7bb75a987e57da40a949c42554ca476d8124dca6a7492cbfc801f7df3dc01d5f | static_analysis |
| ip | 94.154.43.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
