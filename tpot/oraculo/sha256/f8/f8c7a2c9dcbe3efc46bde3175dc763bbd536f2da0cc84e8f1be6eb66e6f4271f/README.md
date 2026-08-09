# 🧬 Payload Analysis

`f8c7a2c9dcbe3efc46bde3175dc763bbd536f2da0cc84e8f1be6eb66e6f4271f`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:08:59+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f8c7a2c9dcbe3efc46bde3175dc763bbd536f2da0cc84e8f1be6eb66e6f4271f`
- **SHA1:** `f9a5ca200860901a41521b94ad163bd180f064e5`
- **MD5:** `6b9c4a493c4f17d11db80417d7f636ac`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 21 B |
| Entropía | 4.2 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | f8c7a2c9dcbe3efc46bde3175dc763bbd536f2da0cc84e8f1be6eb66e6f4271f | static_analysis |
| ip | 91.92.40.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
