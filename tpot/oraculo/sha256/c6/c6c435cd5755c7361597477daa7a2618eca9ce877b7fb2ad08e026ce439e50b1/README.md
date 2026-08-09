# 🧬 Payload Analysis

`c6c435cd5755c7361597477daa7a2618eca9ce877b7fb2ad08e026ce439e50b1`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c6c435cd5755c7361597477daa7a2618eca9ce877b7fb2ad08e026ce439e50b1`
- **SHA1:** `0ffe46d2a97b91a1283a9d2e469f7dd07cf8cedc`
- **MD5:** `ea549a93eaac32f4912d152c1d2e4fbb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 22 B |
| Entropía | 3.88 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | c6c435cd5755c7361597477daa7a2618eca9ce877b7fb2ad08e026ce439e50b1 | static_analysis |
| ip | 4.246.204.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
