# 🧬 Payload Analysis

`da353a2b8f5f0e0dac38a941676723bbf1f0108fb75974b6a1044d6a419a1a8d`

## 📌 Resumen

Artefacto identificado como HTML document, Unicode text, UTF-8 text, with very long lines (1782), with CRLF, LF line terminators de 4.0 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `11` en `hxxp://gmpg[.]org/xfn/11`. Se extrajeron 5 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:32:58.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `da353a2b8f5f0e0dac38a941676723bbf1f0108fb75974b6a1044d6a419a1a8d`
- **SHA1:** `171ce668eb11aac299af9206f7c6316fd0ebd7fe`
- **MD5:** `546c84458a647e13d9bc7daad3b9455e`

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
| url | hxxp://gmpg[.]org/xfn/11 | strings |
| url | hxxp://[internal-ip-redacted]/wp-content/themes/twentyseventeen/assets/css/ie8.css?ver=1.0 | strings |
| url | hxxps://fonts[.]googleapis[.]com/css?family=Libre+Franklin%3A300%2C300i%2C400%2C400i%2C600%2C600i%2C800%2C800i&amp;subset=latin%2Clatin-ext | strings |
| url | hxxps://fonts[.]gstatic[.]com | strings |
| url | hxxp://[internal-ip-redacted]/wp-content/themes/twentyseventeen/assets/js/html5.js?ver=3.7.3 | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | da353a2b8f5f0e0dac38a941676723bbf1f0108fb75974b6a1044d6a419a1a8d | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
