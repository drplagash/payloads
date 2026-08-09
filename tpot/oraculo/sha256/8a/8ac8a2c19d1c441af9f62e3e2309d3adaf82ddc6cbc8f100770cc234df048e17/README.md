# 🧬 Payload Analysis

`8ac8a2c19d1c441af9f62e3e2309d3adaf82ddc6cbc8f100770cc234df048e17`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:59:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8ac8a2c19d1c441af9f62e3e2309d3adaf82ddc6cbc8f100770cc234df048e17`
- **SHA1:** `3e6f99f16b13cf6576708c719f9fe145488e1278`
- **MD5:** `0a986294c226383a13010e69e3182bcb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 18 B |
| Entropía | 3.35 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 8ac8a2c19d1c441af9f62e3e2309d3adaf82ddc6cbc8f100770cc234df048e17 | static_analysis |
| ip | 185.189.182.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
