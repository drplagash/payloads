# 🧬 Payload Analysis

`e0378c80dcf0f44c96b915fb9750e036c90d803f881099d4fa7c42d5cc8456f5`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:57:22+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e0378c80dcf0f44c96b915fb9750e036c90d803f881099d4fa7c42d5cc8456f5`
- **SHA1:** `f68a9cba01cfcca565b47cc5efe095a55985ebd9`
- **MD5:** `8a59a036c48e1129fadf6cfc910cad8a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | OpenPGP Secret Key |
| Tamaño | 21 B |
| Entropía | 4.2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=OpenPGP Secret Key; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | e0378c80dcf0f44c96b915fb9750e036c90d803f881099d4fa7c42d5cc8456f5 | static_analysis |
| ip | 91.92.40.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
