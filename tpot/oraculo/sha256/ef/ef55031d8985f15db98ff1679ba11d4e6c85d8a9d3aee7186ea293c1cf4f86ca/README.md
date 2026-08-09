# 🧬 Payload Analysis

`ef55031d8985f15db98ff1679ba11d4e6c85d8a9d3aee7186ea293c1cf4f86ca`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:02+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ef55031d8985f15db98ff1679ba11d4e6c85d8a9d3aee7186ea293c1cf4f86ca`
- **SHA1:** `6ab82937e00b625d852b700d1947afc6fa7195bc`
- **MD5:** `420b2d6c6bae759eccd54b4bd190edd5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 783 B |
| Entropía | 5.49 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 160.1.3.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | ef55031d8985f15db98ff1679ba11d4e6c85d8a9d3aee7186ea293c1cf4f86ca | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
