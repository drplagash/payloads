# 🧬 Payload Analysis

`082ca9f9deeaee594a952b472a88ba07a3a8ba3fac7524d563c5b0a681ebd20c`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `082ca9f9deeaee594a952b472a88ba07a3a8ba3fac7524d563c5b0a681ebd20c`
- **SHA1:** `1ed40022847757155fe441dc69a038f62e5e4146`
- **MD5:** `207ed5b31ea864028ad0f1917346e79f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 799 B |
| Entropía | 5.53 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 121.201.234.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 082ca9f9deeaee594a952b472a88ba07a3a8ba3fac7524d563c5b0a681ebd20c | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
