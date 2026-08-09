# 🧬 Payload Analysis

`c6f6a00e1fa0aeddfdff94741d3bd08fe35b96eb0eaf92db95f3dba28e45c4a3`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:14:00+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c6f6a00e1fa0aeddfdff94741d3bd08fe35b96eb0eaf92db95f3dba28e45c4a3`
- **SHA1:** `6770d5c4bdd473064635d2393d3456e59f3f3f7c`
- **MD5:** `1754b37b44273a51bf7c243ffa38d8e7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 171 B |
| Entropía | 5.1 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.153.XXX | static_analysis |
| hash | c6f6a00e1fa0aeddfdff94741d3bd08fe35b96eb0eaf92db95f3dba28e45c4a3 | static_analysis |
| ip | 77.83.240.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
