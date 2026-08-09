# 🧬 Payload Analysis

`f943e8d145f9ac79a5b8dc1919eb638620ad775ed43b6e59a2c5cb16244df4ee`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:15:17+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f943e8d145f9ac79a5b8dc1919eb638620ad775ed43b6e59a2c5cb16244df4ee`
- **SHA1:** `b68df323607ac276f9a1c423269c2eb5a37f5bfb`
- **MD5:** `4b363009e36ede717e55988097ee3d12`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 87 B |
| Entropía | 4.9 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.153.XXX | static_analysis |
| hash | f943e8d145f9ac79a5b8dc1919eb638620ad775ed43b6e59a2c5cb16244df4ee | static_analysis |
| ip | 176.65.139.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
