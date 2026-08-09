# 🧬 Payload Analysis

`734635e3c4394ab91272cfbfbe195a15d7cee06dad2e65b75f55535523745125`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `734635e3c4394ab91272cfbfbe195a15d7cee06dad2e65b75f55535523745125`
- **SHA1:** `37a812cdef4e02adee905eba0310265ef2dd6552`
- **MD5:** `4158ec498bb2a319e011665161204a15`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 103 B |
| Entropía | 5.11 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.139.XXX | static_analysis |
| hash | 734635e3c4394ab91272cfbfbe195a15d7cee06dad2e65b75f55535523745125 | static_analysis |
| ip | 93.123.72.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
