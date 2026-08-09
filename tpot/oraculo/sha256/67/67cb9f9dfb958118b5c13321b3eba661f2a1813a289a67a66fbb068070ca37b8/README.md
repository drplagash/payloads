# 🧬 Payload Analysis

`67cb9f9dfb958118b5c13321b3eba661f2a1813a289a67a66fbb068070ca37b8`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:40+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `67cb9f9dfb958118b5c13321b3eba661f2a1813a289a67a66fbb068070ca37b8`
- **SHA1:** `2c7244031634e1752a40fbb0c34b77993110636d`
- **MD5:** `a09764d7c6f716cd67a27e5099b09608`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 549 B |
| Entropía | 5.39 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| hash | 67cb9f9dfb958118b5c13321b3eba661f2a1813a289a67a66fbb068070ca37b8 | static_analysis |
| ip | 141.98.11.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
