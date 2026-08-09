# 🧬 Payload Analysis

`0ea025cd69aba9b87f0b6164c91d0c4bc0a48fd9ef7b157ee6970694445eae7d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:06:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0ea025cd69aba9b87f0b6164c91d0c4bc0a48fd9ef7b157ee6970694445eae7d`
- **SHA1:** `53cfa75fd49a8f5b7e5f825287fc5d203861cd98`
- **MD5:** `b314037d2e9affe35229f70e4d7d54b2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 177 B |
| Entropía | 5.14 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| hash | 0ea025cd69aba9b87f0b6164c91d0c4bc0a48fd9ef7b157ee6970694445eae7d | static_analysis |
| ip | 160.119.76.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
