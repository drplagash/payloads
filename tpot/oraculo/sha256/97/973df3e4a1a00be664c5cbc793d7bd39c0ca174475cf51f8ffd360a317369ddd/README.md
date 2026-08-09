# 🧬 Payload Analysis

`973df3e4a1a00be664c5cbc793d7bd39c0ca174475cf51f8ffd360a317369ddd`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:57:22+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `973df3e4a1a00be664c5cbc793d7bd39c0ca174475cf51f8ffd360a317369ddd`
- **SHA1:** `d3f3c4a52d99cb49cef4b9e2b35ad36e7dd45acd`
- **MD5:** `c993925125ecfd6497d38dc014fa7544`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 96 B |
| Entropía | 4.85 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| hash | 973df3e4a1a00be664c5cbc793d7bd39c0ca174475cf51f8ffd360a317369ddd | static_analysis |
| ip | 178.238.234.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
