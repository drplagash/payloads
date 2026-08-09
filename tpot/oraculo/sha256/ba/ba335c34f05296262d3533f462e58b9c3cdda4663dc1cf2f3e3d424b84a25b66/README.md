# 🧬 Payload Analysis

`ba335c34f05296262d3533f462e58b9c3cdda4663dc1cf2f3e3d424b84a25b66`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:19+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ba335c34f05296262d3533f462e58b9c3cdda4663dc1cf2f3e3d424b84a25b66`
- **SHA1:** `4c8e175539f4fb350dcf8ad9786b0fc5b43f0165`
- **MD5:** `1084dc7b22f225754ad8db70289d9c1b`

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
| ip | 189.71.23.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | ba335c34f05296262d3533f462e58b9c3cdda4663dc1cf2f3e3d424b84a25b66 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
