# 🧬 Payload Analysis

`80f29577b3f940a51f615889e93c3add6daec99367cb679afa5f02b4ec342eb8`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:47+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `80f29577b3f940a51f615889e93c3add6daec99367cb679afa5f02b4ec342eb8`
- **SHA1:** `54a37545e2769cf888c43fe5bd1285b43160625b`
- **MD5:** `44b3d8bbf932b635d7a1194ac24af89b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 64 B |
| Entropía | 4.67 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 80f29577b3f940a51f615889e93c3add6daec99367cb679afa5f02b4ec342eb8 | static_analysis |
| ip | 154.90.70.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
