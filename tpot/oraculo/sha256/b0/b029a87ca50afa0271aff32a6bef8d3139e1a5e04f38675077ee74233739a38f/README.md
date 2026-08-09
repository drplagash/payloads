# 🧬 Payload Analysis

`b029a87ca50afa0271aff32a6bef8d3139e1a5e04f38675077ee74233739a38f`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b029a87ca50afa0271aff32a6bef8d3139e1a5e04f38675077ee74233739a38f`
- **SHA1:** `1bb6b73f3a18d7f52ac0e9beb883f9f06eb61aae`
- **MD5:** `764141dd9761f34d65db0f7bf0ee3d3b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 116 B |
| Entropía | 4.95 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | b029a87ca50afa0271aff32a6bef8d3139e1a5e04f38675077ee74233739a38f | static_analysis |
| ip | 165.227.171.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
