# 🧬 Payload Analysis

`2dc7ab44967f20845cee4cb808457be88f9040f04a58b3e8a3ff6aeb5bdcea61`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:03:20+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2dc7ab44967f20845cee4cb808457be88f9040f04a58b3e8a3ff6aeb5bdcea61`
- **SHA1:** `3b1bf69b83c5b57ed2c4ce374d01608e2b5acf61`
- **MD5:** `de5d421febe13d46c903f4eb87b8dfb1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 24 B |
| Entropía | 4.14 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 2dc7ab44967f20845cee4cb808457be88f9040f04a58b3e8a3ff6aeb5bdcea61 | static_analysis |
| ip | 66.85.30.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
