# 🧬 Payload Analysis

`313c6c74ae1f96bb5c375a0d422867759240e3e1e886a23b64cf8c07fc0eb3da`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:58+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `313c6c74ae1f96bb5c375a0d422867759240e3e1e886a23b64cf8c07fc0eb3da`
- **MD5:** `ec17fd6327affc3369a21365eabb1b02`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (377), with CRLF line terminators |
| Tamaño | 1.1 KiB |
| Entropía | 5.63 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (377), with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 120.0.0.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| hash | 313c6c74ae1f96bb5c375a0d422867759240e3e1e886a23b64cf8c07fc0eb3da | static_analysis |
| ip | 20.193.146.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
