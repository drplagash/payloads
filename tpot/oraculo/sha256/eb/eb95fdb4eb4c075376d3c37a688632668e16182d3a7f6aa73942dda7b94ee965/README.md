# 🧬 Payload Analysis

`eb95fdb4eb4c075376d3c37a688632668e16182d3a7f6aa73942dda7b94ee965`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:05:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `eb95fdb4eb4c075376d3c37a688632668e16182d3a7f6aa73942dda7b94ee965`
- **SHA1:** `f2e82af741c7036970213a782ce731f5265bfded`
- **MD5:** `6aec696e70c031fb93c9269a6bf72b4c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 106 B |
| Entropía | 4.94 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.160.XXX | static_analysis |
| hash | eb95fdb4eb4c075376d3c37a688632668e16182d3a7f6aa73942dda7b94ee965 | static_analysis |
| ip | 142.93.105.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
