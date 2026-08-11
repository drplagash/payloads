# 🧬 Payload Analysis

`c5ecd752bf39fbababcdd93d5b70620215b365862d412bdf0cc565d121d6c3f2`

## 📌 Resumen

Texto Unicode de 4.0 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `ie8.css` en `hxxp://[internal-ip-redacted]/wp-content/themes/twentyseventeen/assets/css/ie8.css`. **C2 / infraestructura de control:**

- **Posible C2:** `[internal-ip-redacted]` — confianza Medio, evidencia hardcoded_in_payload Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/c5ecd752bf39fbababcdd93d5b70620215b365862d412bdf0cc565d121d6c3f2.md](../../../../../malware-like/oraculo/downloader/c5ecd752bf39fbababcdd93d5b70620215b365862d412bdf0cc565d121d6c3f2.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c5ecd752bf39fbababcdd93d5b70620215b365862d412bdf0cc565d121d6c3f2`
- **SHA1:** `5a67d597c9317261f7aedf118e4496e4b27c51ef`
- **MD5:** `6b5c6b0fd1326dca9694293c5bdb9e2d`

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
| url | hxxp://[internal-ip-redacted]/wp-content/themes/twentyseventeen/assets/css/ie8.css?ver=1.0 | strings |
| url | hxxps://fonts[.]gstatic[.]com | strings |
| url | hxxp://gmpg[.]org/xfn/11 | strings |
| url | hxxps://fonts[.]googleapis[.]com/css?family=Libre+Franklin%3A300%2C300i%2C400%2C400i%2C600%2C600i%2C800%2C800i&amp;subset=latin%2Clatin-ext | strings |
| url | hxxp://[internal-ip-redacted]/wp-content/themes/twentyseventeen/assets/js/html5.js?ver=3.7.3 | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | c5ecd752bf39fbababcdd93d5b70620215b365862d412bdf0cc565d121d6c3f2 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
