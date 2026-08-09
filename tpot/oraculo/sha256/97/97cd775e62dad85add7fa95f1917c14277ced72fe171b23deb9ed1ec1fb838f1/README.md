# 🧬 Payload Analysis

`97cd775e62dad85add7fa95f1917c14277ced72fe171b23deb9ed1ec1fb838f1`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:14:00+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `97cd775e62dad85add7fa95f1917c14277ced72fe171b23deb9ed1ec1fb838f1`
- **SHA1:** `b0a324846fe55bba46771ffb0a91d164878960d4`
- **MD5:** `570eb2e917097f5e7ba6a70b182420ad`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 171 B |
| Entropía | 5.09 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.153.XXX | static_analysis |
| hash | 97cd775e62dad85add7fa95f1917c14277ced72fe171b23deb9ed1ec1fb838f1 | static_analysis |
| ip | 77.83.240.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
