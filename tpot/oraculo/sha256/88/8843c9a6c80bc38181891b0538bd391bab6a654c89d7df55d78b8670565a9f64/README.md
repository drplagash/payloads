# 🧬 Payload Analysis

`8843c9a6c80bc38181891b0538bd391bab6a654c89d7df55d78b8670565a9f64`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:56+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8843c9a6c80bc38181891b0538bd391bab6a654c89d7df55d78b8670565a9f64`
- **SHA1:** `0224c6a9c62e4a1c7f24d90d7fa403954529dc6f`
- **MD5:** `f3ddd2050cde28d8050bf9cf187ed4d1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 21 B |
| Entropía | 4.11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 8843c9a6c80bc38181891b0538bd391bab6a654c89d7df55d78b8670565a9f64 | static_analysis |
| ip | 110.39.255.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
