# 🧬 Payload Analysis

`0b4494d64e9f3a8e44c68d15bf6f6cd9bdca583d2abfa1208c2080e27aa3e08d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:16+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0b4494d64e9f3a8e44c68d15bf6f6cd9bdca583d2abfa1208c2080e27aa3e08d`
- **SHA1:** `7c491d1c22c5c52ea2e1076022e5497759f32e67`
- **MD5:** `34148f6f8aa1eec7c1faae22f87d40f6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 734 B |
| Entropía | 5.36 |
| Strings | 22 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | 0b4494d64e9f3a8e44c68d15bf6f6cd9bdca583d2abfa1208c2080e27aa3e08d | static_analysis |
| ip | 87.106.98.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
