# 🧬 Payload Analysis

`a5f73bd0623fbebe0e4631faa0187bc06623f1cead5a7f2f6648cdacfa18f014`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:37:42+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a5f73bd0623fbebe0e4631faa0187bc06623f1cead5a7f2f6648cdacfa18f014`
- **SHA1:** `0f4237f48d74042fea49af70e0f450330c5ae4c2`
- **MD5:** `8402758ff821a7cea1d2b4bb01460190`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 69 B |
| Entropía | 4.82 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | a5f73bd0623fbebe0e4631faa0187bc06623f1cead5a7f2f6648cdacfa18f014 | static_analysis |
| ip | 5.61.209.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
