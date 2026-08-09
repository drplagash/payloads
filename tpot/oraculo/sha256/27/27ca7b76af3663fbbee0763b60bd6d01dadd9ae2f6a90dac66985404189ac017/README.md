# 🧬 Payload Analysis

`27ca7b76af3663fbbee0763b60bd6d01dadd9ae2f6a90dac66985404189ac017`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:54:25+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `27ca7b76af3663fbbee0763b60bd6d01dadd9ae2f6a90dac66985404189ac017`
- **SHA1:** `a6625f5ecbedc13df6464fbe33adf1c66780257c`
- **MD5:** `c81d7a203bfb492449aa50d912d05c43`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 22 B |
| Entropía | 4.19 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 27ca7b76af3663fbbee0763b60bd6d01dadd9ae2f6a90dac66985404189ac017 | static_analysis |
| ip | 59.11.42.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
