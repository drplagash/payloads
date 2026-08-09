# 🧬 Payload Analysis

`41849f087008a50a6f92d59658c3545e75826621e46ed0d7e8d9a77edd2973b6`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:14:00+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `41849f087008a50a6f92d59658c3545e75826621e46ed0d7e8d9a77edd2973b6`
- **SHA1:** `7972b859253e1fbd50425362bbc06c300f5bd6a3`
- **MD5:** `b09067085ab588125e11311a019d56eb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 171 B |
| Entropía | 5.11 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.153.XXX | static_analysis |
| hash | 41849f087008a50a6f92d59658c3545e75826621e46ed0d7e8d9a77edd2973b6 | static_analysis |
| ip | 77.83.240.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
