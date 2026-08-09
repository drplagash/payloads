# 🧬 Payload Analysis

`8b4c60a8e1e2c39b6f8e91a2fa7b6b839e5cc3ef2d69c75f0512b86d65519af6`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:36:13+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8b4c60a8e1e2c39b6f8e91a2fa7b6b839e5cc3ef2d69c75f0512b86d65519af6`
- **MD5:** `e900172fee6744183d88f88c815f5736`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 417 B |
| Entropía | 5.39 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 190.179.174.XXX | static_analysis |
| ip | 217.160.254.XXX | static_analysis |
| hash | 8b4c60a8e1e2c39b6f8e91a2fa7b6b839e5cc3ef2d69c75f0512b86d65519af6 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
