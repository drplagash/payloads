# 🧬 Payload Analysis

`dac744a3bc6f5e601c1d043bbbd5bf1c8961859a35801caec24181e9f89ea23e`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:37:19+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dac744a3bc6f5e601c1d043bbbd5bf1c8961859a35801caec24181e9f89ea23e`
- **MD5:** `643e370c15561c75653102b32a9d24ee`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 797 B |
| Entropía | 5.49 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.175.XXX | static_analysis |
| ip | 197.10.84.XXX | static_analysis |
| hash | dac744a3bc6f5e601c1d043bbbd5bf1c8961859a35801caec24181e9f89ea23e | static_analysis |
| ip | 144.172.106.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
