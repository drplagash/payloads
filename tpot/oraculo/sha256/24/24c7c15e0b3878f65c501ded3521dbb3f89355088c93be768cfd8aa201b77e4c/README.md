# 🧬 Payload Analysis

`24c7c15e0b3878f65c501ded3521dbb3f89355088c93be768cfd8aa201b77e4c`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:10:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `24c7c15e0b3878f65c501ded3521dbb3f89355088c93be768cfd8aa201b77e4c`
- **SHA1:** `3a55b48d8afe3bf33615469a1e5c933a51b671e6`
- **MD5:** `74bd62bb2ebf6129dc9aa0ea93008511`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 69 B |
| Entropía | 4.89 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.166.XXX | static_analysis |
| hash | 24c7c15e0b3878f65c501ded3521dbb3f89355088c93be768cfd8aa201b77e4c | static_analysis |
| ip | 5.61.209.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
