# 🧬 Payload Analysis

`a0f9201bcac6d0912565c7cbd5030ae8ff9e6e4eef7c28c6c73cb2a6208a1c57`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:15:17+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a0f9201bcac6d0912565c7cbd5030ae8ff9e6e4eef7c28c6c73cb2a6208a1c57`
- **SHA1:** `f5c2b0e7f0e7b9bba4d1543b77319e541a919e00`
- **MD5:** `2270dfc4fb7835e995c1ff5577f4698b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | HTML document, Unicode text, UTF-8 text, with very long lines (1782), with CRLF, LF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.6 |
| Strings | 46 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=HTML document, Unicode text, UTF-8 text, with very long lines (1782), with CRLF, LF line terminators; iocs=7

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | [internal-ip-redacted] | static_analysis |
| url | hxxp://[internal-ip-redacted]/wp-content/themes/twentyseventeen/assets/css/ie8.css?ver=1.0 | strings |
| url | hxxp://[internal-ip-redacted]/wp-content/themes/twentyseventeen/assets/js/html5.js?ver=3.7.3 | strings |
| url | hxxp://gmpg[.]org/xfn/11 | strings |
| url | hxxps://fonts[.]googleapis[.]com/css?family=Libre+Franklin%3A300%2C300i%2C400%2C400i%2C600%2C600i%2C800%2C800i&amp;subset=latin%2Clatin-ext | strings |
| url | hxxps://fonts[.]gstatic[.]com | strings |
| hash | a0f9201bcac6d0912565c7cbd5030ae8ff9e6e4eef7c28c6c73cb2a6208a1c57 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
