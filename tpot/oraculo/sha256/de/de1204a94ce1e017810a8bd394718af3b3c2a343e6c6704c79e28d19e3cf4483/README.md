# 🧬 Payload Analysis

`de1204a94ce1e017810a8bd394718af3b3c2a343e6c6704c79e28d19e3cf4483`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:49:32+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `de1204a94ce1e017810a8bd394718af3b3c2a343e6c6704c79e28d19e3cf4483`
- **SHA1:** `5993eaec104387a802606f7c284df8ad1c0a4b7e`
- **MD5:** `cb0d6606e2a9060c2c11926669bdf551`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.48 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | [internal-ip-redacted] | static_analysis |
| url | hxxp://[internal-ip-redacted]/index.php?title=Main_Page&amp;oldid=1 | strings |
| hash | de1204a94ce1e017810a8bd394718af3b3c2a343e6c6704c79e28d19e3cf4483 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
