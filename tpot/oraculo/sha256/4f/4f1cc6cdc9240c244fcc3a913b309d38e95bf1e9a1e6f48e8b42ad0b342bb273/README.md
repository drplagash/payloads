# 🧬 Payload Analysis

`4f1cc6cdc9240c244fcc3a913b309d38e95bf1e9a1e6f48e8b42ad0b342bb273`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:10:14+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4f1cc6cdc9240c244fcc3a913b309d38e95bf1e9a1e6f48e8b42ad0b342bb273`
- **SHA1:** `4c65e144d1590a0475ca442137a029c1d3f44962`
- **MD5:** `9e083097e534ebcda29d75b531e97f38`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Non-ISO extended-ASCII text, with no line terminators, with escape sequences |
| Tamaño | 90 B |
| Entropía | 5.66 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Non-ISO extended-ASCII text, with no line terminators, with escape sequences; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 4f1cc6cdc9240c244fcc3a913b309d38e95bf1e9a1e6f48e8b42ad0b342bb273 | static_analysis |
| ip | 5.83.143.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
