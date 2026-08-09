# 🧬 Payload Analysis

`0a1b9e2ad86e4123a1b24fb69f2b7a8a6e161c534cab4bbffa81e11a33c1c9ec`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:00:21+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0a1b9e2ad86e4123a1b24fb69f2b7a8a6e161c534cab4bbffa81e11a33c1c9ec`
- **SHA1:** `77eefe2649c9933a4f8e217be3eba5a3549651de`
- **MD5:** `3032a4dbd65966a00cca072831859015`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 27 B |
| Entropía | 4.36 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 0a1b9e2ad86e4123a1b24fb69f2b7a8a6e161c534cab4bbffa81e11a33c1c9ec | static_analysis |
| ip | 187.110.238.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
