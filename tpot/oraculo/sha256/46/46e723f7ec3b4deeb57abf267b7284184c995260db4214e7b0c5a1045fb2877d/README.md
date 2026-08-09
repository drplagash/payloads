# 🧬 Payload Analysis

`46e723f7ec3b4deeb57abf267b7284184c995260db4214e7b0c5a1045fb2877d`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:19:06+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `46e723f7ec3b4deeb57abf267b7284184c995260db4214e7b0c5a1045fb2877d`
- **SHA1:** `2a1d8e121bcc27cb1de1599644a28c150a83ca27`
- **MD5:** `3faa27524f13920bb54eb2c9e7cccbea`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 62 B |
| Entropía | 4.51 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 46e723f7ec3b4deeb57abf267b7284184c995260db4214e7b0c5a1045fb2877d | static_analysis |
| ip | 176.65.148.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
