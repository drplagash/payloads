# 🧬 Payload Analysis

`89bf7a81aaa80e0f3aab8d57d6c504025d665f3d1eb4cc85bd8f34c4d9e09b93`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:56+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `89bf7a81aaa80e0f3aab8d57d6c504025d665f3d1eb4cc85bd8f34c4d9e09b93`
- **SHA1:** `fc6ba205dd60999949d35cd84cf784df632925bd`
- **MD5:** `46db56270563c044faff157ac552df25`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 700 B |
| Entropía | 5.43 |
| Strings | 21 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.144.XXX | static_analysis |
| hash | 89bf7a81aaa80e0f3aab8d57d6c504025d665f3d1eb4cc85bd8f34c4d9e09b93 | static_analysis |
| ip | 89.190.156.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
