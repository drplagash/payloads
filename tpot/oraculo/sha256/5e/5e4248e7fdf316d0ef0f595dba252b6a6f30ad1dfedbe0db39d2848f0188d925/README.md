# 🧬 Payload Analysis

`5e4248e7fdf316d0ef0f595dba252b6a6f30ad1dfedbe0db39d2848f0188d925`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5e4248e7fdf316d0ef0f595dba252b6a6f30ad1dfedbe0db39d2848f0188d925`
- **SHA1:** `aa6208710384ac785140a4fd32b5f9756023ff10`
- **MD5:** `3d6743eba11749f06bb0a3907140c4c0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | HTML document, Unicode text, UTF-8 text, with CRLF, LF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.17 |
| Strings | 111 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=HTML document, Unicode text, UTF-8 text, with CRLF, LF line terminators; strings=111; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://fonts[.]googleapis[.]com/css?family=Open+Sans | strings |
| hash | 5e4248e7fdf316d0ef0f595dba252b6a6f30ad1dfedbe0db39d2848f0188d925 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
