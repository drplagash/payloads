# 🧬 Payload Analysis

`834ab8117330d36fda061ddcd9b8da1f2cd8c319e5e8d66621a724a2db0962e2`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:58+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `834ab8117330d36fda061ddcd9b8da1f2cd8c319e5e8d66621a724a2db0962e2`
- **MD5:** `bfe4163db78ebb1fa4c9f22c413b68db`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 791 B |
| Entropía | 5.47 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 15.26.1.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| hash | 834ab8117330d36fda061ddcd9b8da1f2cd8c319e5e8d66621a724a2db0962e2 | static_analysis |
| ip | 144.172.106.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
