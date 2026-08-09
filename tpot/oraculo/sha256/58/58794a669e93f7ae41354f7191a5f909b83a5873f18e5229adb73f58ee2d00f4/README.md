# 🧬 Payload Analysis

`58794a669e93f7ae41354f7191a5f909b83a5873f18e5229adb73f58ee2d00f4`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:29:35+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `58794a669e93f7ae41354f7191a5f909b83a5873f18e5229adb73f58ee2d00f4`
- **SHA1:** `cb904ac1d48648e871514a1be3d271317805c2ad`
- **MD5:** `48509b8bbba58c28a8285eb8b8cac6c3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.38 |
| Strings | 12 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | [internal-ip-redacted] | static_analysis |
| url | hxxp://[internal-ip-redacted]/Status_404 | strings |
| hash | 58794a669e93f7ae41354f7191a5f909b83a5873f18e5229adb73f58ee2d00f4 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
