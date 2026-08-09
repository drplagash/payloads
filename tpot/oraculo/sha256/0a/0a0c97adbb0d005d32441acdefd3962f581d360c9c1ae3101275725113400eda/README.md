# 🧬 Payload Analysis

`0a0c97adbb0d005d32441acdefd3962f581d360c9c1ae3101275725113400eda`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:31:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0a0c97adbb0d005d32441acdefd3962f581d360c9c1ae3101275725113400eda`
- **SHA1:** `aa38d72e52ecd4e7e27e85b85b3432d7976cdff1`
- **MD5:** `e8233c8c3a4d37cda26721e75485cac9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 212 B |
| Entropía | 5.45 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | 0a0c97adbb0d005d32441acdefd3962f581d360c9c1ae3101275725113400eda | static_analysis |
| ip | 213.209.159.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
