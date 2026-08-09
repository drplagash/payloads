# 🧬 Payload Analysis

`09664be8aafbdd1e08b9bfee125636ec0504b7a5baa34288c7ad0e526280cafe`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:01:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `09664be8aafbdd1e08b9bfee125636ec0504b7a5baa34288c7ad0e526280cafe`
- **SHA1:** `8c47df6e8194c25cbecc501921fb30ecbacddc16`
- **MD5:** `1243c46e77d3d33d36b1ddee29e699e5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 942 B |
| Entropía | 5.66 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 134.0.0.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 09664be8aafbdd1e08b9bfee125636ec0504b7a5baa34288c7ad0e526280cafe | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
