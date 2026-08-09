# 🧬 Payload Analysis

`181eb17a7e6b92013f7375c0938611af7677e39326c8687a35b00bdfdf5c6f78`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:10+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `181eb17a7e6b92013f7375c0938611af7677e39326c8687a35b00bdfdf5c6f78`
- **SHA1:** `9940010273d9e9d5f31c8b66bea34c30875c9fc9`
- **MD5:** `af95d826fbb3dce8c1a4c15a622c734f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 117 B |
| Entropía | 5.1 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | 181eb17a7e6b92013f7375c0938611af7677e39326c8687a35b00bdfdf5c6f78 | static_analysis |
| ip | 20.64.105.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
