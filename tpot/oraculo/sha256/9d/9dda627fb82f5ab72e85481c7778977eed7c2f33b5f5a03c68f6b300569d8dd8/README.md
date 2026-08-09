# 🧬 Payload Analysis

`9dda627fb82f5ab72e85481c7778977eed7c2f33b5f5a03c68f6b300569d8dd8`

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

- **SHA256:** `9dda627fb82f5ab72e85481c7778977eed7c2f33b5f5a03c68f6b300569d8dd8`
- **SHA1:** `4a3bebfd294ffd2fba382386db2d1762abcc64eb`
- **MD5:** `09a8242e400b628e35fd6abd5b6fc82c`

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
| hash | 9dda627fb82f5ab72e85481c7778977eed7c2f33b5f5a03c68f6b300569d8dd8 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
