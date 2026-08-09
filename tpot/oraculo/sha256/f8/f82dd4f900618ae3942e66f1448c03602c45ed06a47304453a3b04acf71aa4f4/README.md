# 🧬 Payload Analysis

`f82dd4f900618ae3942e66f1448c03602c45ed06a47304453a3b04acf71aa4f4`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f82dd4f900618ae3942e66f1448c03602c45ed06a47304453a3b04acf71aa4f4`
- **SHA1:** `23aafe508503fbbac359917ad5815a4bbabba336`
- **MD5:** `21812fc75ab90aad38426600a85dd073`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 21 B |
| Entropía | 4.2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | f82dd4f900618ae3942e66f1448c03602c45ed06a47304453a3b04acf71aa4f4 | static_analysis |
| ip | 91.92.40.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
