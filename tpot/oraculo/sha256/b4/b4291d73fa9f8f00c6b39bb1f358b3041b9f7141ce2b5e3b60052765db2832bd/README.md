# 🧬 Payload Analysis

`b4291d73fa9f8f00c6b39bb1f358b3041b9f7141ce2b5e3b60052765db2832bd`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b4291d73fa9f8f00c6b39bb1f358b3041b9f7141ce2b5e3b60052765db2832bd`
- **SHA1:** `b78ec7ea863d38e272cb1735744270bd84e535d8`
- **MD5:** `3a009081d2c6c5c4dbaa3d7d99a61629`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 144 B |
| Entropía | 5.09 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.160.XXX | static_analysis |
| hash | b4291d73fa9f8f00c6b39bb1f358b3041b9f7141ce2b5e3b60052765db2832bd | static_analysis |
| ip | 185.242.226.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
