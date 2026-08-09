# 🧬 Payload Analysis

`808a2f230366c08f09a10f4a9c2c00c17aacaf3c7edf5570e53b5605462a4c2b`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:19:44+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `808a2f230366c08f09a10f4a9c2c00c17aacaf3c7edf5570e53b5605462a4c2b`
- **SHA1:** `9b61dd060297cf1804b16d3676662cf6c17924f0`
- **MD5:** `0f86113aa47764006948061ec669a593`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 24 B |
| Entropía | 4.17 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 808a2f230366c08f09a10f4a9c2c00c17aacaf3c7edf5570e53b5605462a4c2b | static_analysis |
| ip | 193.46.255.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
