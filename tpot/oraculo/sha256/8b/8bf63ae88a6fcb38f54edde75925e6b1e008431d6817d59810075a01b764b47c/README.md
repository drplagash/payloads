# 🧬 Payload Analysis

`8bf63ae88a6fcb38f54edde75925e6b1e008431d6817d59810075a01b764b47c`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:37:19+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8bf63ae88a6fcb38f54edde75925e6b1e008431d6817d59810075a01b764b47c`
- **MD5:** `f5405b855568fb0c0155597deb367f61`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 984 B |
| Entropía | 5.69 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.174.XXX | static_analysis |
| hash | 8bf63ae88a6fcb38f54edde75925e6b1e008431d6817d59810075a01b764b47c | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
