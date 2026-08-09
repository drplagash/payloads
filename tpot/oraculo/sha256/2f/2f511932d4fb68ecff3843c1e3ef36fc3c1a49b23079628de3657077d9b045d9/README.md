# 🧬 Payload Analysis

`2f511932d4fb68ecff3843c1e3ef36fc3c1a49b23079628de3657077d9b045d9`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:20:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2f511932d4fb68ecff3843c1e3ef36fc3c1a49b23079628de3657077d9b045d9`
- **SHA1:** `2b5312c3b42b9a264c0d2cd74f3c7f229123d085`
- **MD5:** `3636961350331601af597adb2561259d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 61 B |
| Entropía | 4.46 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 2f511932d4fb68ecff3843c1e3ef36fc3c1a49b23079628de3657077d9b045d9 | static_analysis |
| ip | 176.65.148.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
