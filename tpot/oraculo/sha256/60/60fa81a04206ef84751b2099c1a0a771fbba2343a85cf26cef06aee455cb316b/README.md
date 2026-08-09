# 🧬 Payload Analysis

`60fa81a04206ef84751b2099c1a0a771fbba2343a85cf26cef06aee455cb316b`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:22:59+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `60fa81a04206ef84751b2099c1a0a771fbba2343a85cf26cef06aee455cb316b`
- **SHA1:** `a0e67c2a73165824c752f26084b70d1dbf5fb4c1`
- **MD5:** `eaed2bf871c2f49153fa4dd8baad5a2d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 121 B |
| Entropía | 5.25 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| hash | 60fa81a04206ef84751b2099c1a0a771fbba2343a85cf26cef06aee455cb316b | static_analysis |
| ip | 159.89.30.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
