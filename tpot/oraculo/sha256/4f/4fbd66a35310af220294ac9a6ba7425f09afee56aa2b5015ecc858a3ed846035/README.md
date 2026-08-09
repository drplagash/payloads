# 🧬 Payload Analysis

`4fbd66a35310af220294ac9a6ba7425f09afee56aa2b5015ecc858a3ed846035`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:25+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4fbd66a35310af220294ac9a6ba7425f09afee56aa2b5015ecc858a3ed846035`
- **MD5:** `399532398c418cec477e66d5e8c94000`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 618 B |
| Entropía | 5.75 |
| Strings | 14 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 172.110.223.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| hash | 4fbd66a35310af220294ac9a6ba7425f09afee56aa2b5015ecc858a3ed846035 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
