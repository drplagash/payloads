# 🧬 Payload Analysis

`57c210e6b1da2e49a7547bad8074064073b24a76c6a4a03aa4a5473c132a1ee4`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:05:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `57c210e6b1da2e49a7547bad8074064073b24a76c6a4a03aa4a5473c132a1ee4`
- **SHA1:** `729bbe7515140942378091278a6faab4fff0476e`
- **MD5:** `69db979543b542439ad00cbba50fca90`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 106 B |
| Entropía | 4.89 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.160.XXX | static_analysis |
| hash | 57c210e6b1da2e49a7547bad8074064073b24a76c6a4a03aa4a5473c132a1ee4 | static_analysis |
| ip | 152.42.231.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
