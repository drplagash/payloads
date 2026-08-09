# 🧬 Payload Analysis

`7e73d84676d0d9316bc18ed13ab6502c2d7f7dbe8544a415e5c31c5f6171806e`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7e73d84676d0d9316bc18ed13ab6502c2d7f7dbe8544a415e5c31c5f6171806e`
- **SHA1:** `04ac81e075ca8eaf0ba9e5179b87140fbfb44665`
- **MD5:** `d95c50fbe0c06f127157b7851ba44f65`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 24 B |
| Entropía | 4.33 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 7e73d84676d0d9316bc18ed13ab6502c2d7f7dbe8544a415e5c31c5f6171806e | static_analysis |
| ip | 213.177.179.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
