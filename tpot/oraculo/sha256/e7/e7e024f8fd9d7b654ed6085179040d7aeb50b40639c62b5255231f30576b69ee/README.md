# 🧬 Payload Analysis

`e7e024f8fd9d7b654ed6085179040d7aeb50b40639c62b5255231f30576b69ee`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:05:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e7e024f8fd9d7b654ed6085179040d7aeb50b40639c62b5255231f30576b69ee`
- **SHA1:** `f5f3d1d97f3ff92749681b58c52e09afbf36964d`
- **MD5:** `9f95a90b883bc7cef03c5d28440fb65c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 116 B |
| Entropía | 4.93 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.160.XXX | static_analysis |
| hash | e7e024f8fd9d7b654ed6085179040d7aeb50b40639c62b5255231f30576b69ee | static_analysis |
| ip | 165.245.247.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
