# 🧬 Payload Analysis

`1f5844ea110489a8ffd53db123e8d36d20962d53e265312297a580a521b4bf5e`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:07+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1f5844ea110489a8ffd53db123e8d36d20962d53e265312297a580a521b4bf5e`
- **SHA1:** `cfb5364068b78af043f73a30411e82b67125339b`
- **MD5:** `1d118847e07e6737f747f730147b06e0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 32 B |
| Entropía | 4.81 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 1f5844ea110489a8ffd53db123e8d36d20962d53e265312297a580a521b4bf5e | static_analysis |
| ip | 101.96.202.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
