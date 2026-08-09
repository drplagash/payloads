# 🧬 Payload Analysis

`946184a54a47c2c4700924ef825f1b9715fce93d70459f1fd129f1935444d044`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:56:43+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `946184a54a47c2c4700924ef825f1b9715fce93d70459f1fd129f1935444d044`
- **SHA1:** `a34386430a769bd98ff7a2cdd110f067bf52d7df`
- **MD5:** `9584bf43c62255dad349c10398000f4a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 216 B |
| Entropía | 5.38 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 124.0.0.XXX | static_analysis |
| ip | 190.179.144.XXX | static_analysis |
| hash | 946184a54a47c2c4700924ef825f1b9715fce93d70459f1fd129f1935444d044 | static_analysis |
| ip | 64.236.142.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
