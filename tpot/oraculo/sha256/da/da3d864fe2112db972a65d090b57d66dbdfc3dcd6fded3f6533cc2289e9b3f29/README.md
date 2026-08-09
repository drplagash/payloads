# 🧬 Payload Analysis

`da3d864fe2112db972a65d090b57d66dbdfc3dcd6fded3f6533cc2289e9b3f29`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:46:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `da3d864fe2112db972a65d090b57d66dbdfc3dcd6fded3f6533cc2289e9b3f29`
- **SHA1:** `216fab6b63b6535b59f035bccc0f0bb08a6c8fd0`
- **MD5:** `6d77b1f2c88d516169b8623a90b65b2c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 24 B |
| Entropía | 3.72 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | da3d864fe2112db972a65d090b57d66dbdfc3dcd6fded3f6533cc2289e9b3f29 | static_analysis |
| ip | 152.32.174.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
