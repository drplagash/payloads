# 🧬 Payload Analysis

`60fa84ff91c284219d4415024a83ad26383ee57cf3bd50e2f89aafabcbdee36e`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:29:35+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `60fa84ff91c284219d4415024a83ad26383ee57cf3bd50e2f89aafabcbdee36e`
- **SHA1:** `a50b655b3097223228cf3e68c9bca1b8a2af3e49`
- **MD5:** `00977cc68c9b8a806601f1d3a0b54146`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 176 B |
| Entropía | 5.11 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | 60fa84ff91c284219d4415024a83ad26383ee57cf3bd50e2f89aafabcbdee36e | static_analysis |
| ip | 45.95.147.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
