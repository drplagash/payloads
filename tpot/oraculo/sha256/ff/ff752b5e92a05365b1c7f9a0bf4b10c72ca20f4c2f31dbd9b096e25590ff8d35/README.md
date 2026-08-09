# 🧬 Payload Analysis

`ff752b5e92a05365b1c7f9a0bf4b10c72ca20f4c2f31dbd9b096e25590ff8d35`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:14:00+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ff752b5e92a05365b1c7f9a0bf4b10c72ca20f4c2f31dbd9b096e25590ff8d35`
- **SHA1:** `5d5518519957be0f91111e3d68283f1f327b07f1`
- **MD5:** `3e29a98aefcd44fd247b5a6a9c7307a3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 171 B |
| Entropía | 5.12 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.153.XXX | static_analysis |
| hash | ff752b5e92a05365b1c7f9a0bf4b10c72ca20f4c2f31dbd9b096e25590ff8d35 | static_analysis |
| ip | 77.83.240.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
