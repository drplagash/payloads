# 🧬 Payload Analysis

`3ecc247fbdb98e51e0d52c439165ac44ebd4f5ad4135b90888654e5cb29feaca`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:25+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3ecc247fbdb98e51e0d52c439165ac44ebd4f5ad4135b90888654e5cb29feaca`
- **MD5:** `ca59d006ecdd995667fe78a841fc166f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.2 KiB |
| Entropía | 5.37 |
| Strings | 38 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 144.172.93.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| hash | 3ecc247fbdb98e51e0d52c439165ac44ebd4f5ad4135b90888654e5cb29feaca | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
