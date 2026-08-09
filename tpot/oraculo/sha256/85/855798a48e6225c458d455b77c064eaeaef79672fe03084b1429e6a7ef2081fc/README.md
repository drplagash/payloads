# 🧬 Payload Analysis

`855798a48e6225c458d455b77c064eaeaef79672fe03084b1429e6a7ef2081fc`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:01:00+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `855798a48e6225c458d455b77c064eaeaef79672fe03084b1429e6a7ef2081fc`
- **SHA1:** `7d503c30765dbd5105d0e029e533d7ba16626158`
- **MD5:** `e7c7177ba0b364df4d373924472119ac`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Unicode text, UTF-8 text, with CRLF line terminators |
| Tamaño | 1.1 KiB |
| Entropía | 5.65 |
| Strings | 35 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Unicode text, UTF-8 text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 160.119.71.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 855798a48e6225c458d455b77c064eaeaef79672fe03084b1429e6a7ef2081fc | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
