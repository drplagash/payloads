# 🧬 Payload Analysis

`63ef4e72652230faed1928689e3fbc0526ae24c16eac9dbe3c94097606a8dabd`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:48:49+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `63ef4e72652230faed1928689e3fbc0526ae24c16eac9dbe3c94097606a8dabd`
- **SHA1:** `433fd111f68b3b0cedfb053f7bb1aa70ca77d45b`
- **MD5:** `bdb6a173f46b47e9cf263e2b4c54c6d0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF, CR line terminators |
| Tamaño | 137 B |
| Entropía | 5.28 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF, CR line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 239.255.255.XXX | static_analysis |
| hash | 63ef4e72652230faed1928689e3fbc0526ae24c16eac9dbe3c94097606a8dabd | static_analysis |
| ip | 47.77.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
