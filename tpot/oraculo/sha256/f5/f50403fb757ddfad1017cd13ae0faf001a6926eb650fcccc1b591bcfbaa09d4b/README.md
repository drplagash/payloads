# 🧬 Payload Analysis

`f50403fb757ddfad1017cd13ae0faf001a6926eb650fcccc1b591bcfbaa09d4b`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:10:14+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f50403fb757ddfad1017cd13ae0faf001a6926eb650fcccc1b591bcfbaa09d4b`
- **SHA1:** `97819a16bc66f6fabf397aad8f6c7228a5ace053`
- **MD5:** `8661a023dee23af467cf960848b06b5f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (377), with CRLF line terminators |
| Tamaño | 690 B |
| Entropía | 5.48 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (377), with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | f50403fb757ddfad1017cd13ae0faf001a6926eb650fcccc1b591bcfbaa09d4b | static_analysis |
| ip | 198.50.239.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
