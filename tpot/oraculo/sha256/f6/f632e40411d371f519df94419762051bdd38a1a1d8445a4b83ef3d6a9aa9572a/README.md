# 🧬 Payload Analysis

`f632e40411d371f519df94419762051bdd38a1a1d8445a4b83ef3d6a9aa9572a`

## 📌 Resumen

Texto Unicode de 4.0 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `html5.js` en `hxxp://[internal-ip-redacted]/wp-content/themes/twentyseventeen/assets/js/html5.js`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/f632e40411d371f519df94419762051bdd38a1a1d8445a4b83ef3d6a9aa9572a.md](../../../../../malware-like/oraculo/downloader/f632e40411d371f519df94419762051bdd38a1a1d8445a4b83ef3d6a9aa9572a.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:15:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f632e40411d371f519df94419762051bdd38a1a1d8445a4b83ef3d6a9aa9572a`
- **SHA1:** `4658fc5c31fd488bc58adde519cc5ace8ae723ac`
- **MD5:** `95df985db09c4a8a772d463fc3218638`

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
| url | hxxp://[internal-ip-redacted]/wp-content/themes/twentyseventeen/assets/js/html5.js?ver=3.7.3 | strings |
| url | hxxps://fonts[.]gstatic[.]com | strings |
| url | hxxps://fonts[.]googleapis[.]com/css?family=Libre+Franklin%3A300%2C300i%2C400%2C400i%2C600%2C600i%2C800%2C800i&amp;subset=latin%2Clatin-ext | strings |
| url | hxxp://[internal-ip-redacted]/wp-content/themes/twentyseventeen/assets/css/ie8.css?ver=1.0 | strings |
| url | hxxp://gmpg[.]org/xfn/11 | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | f632e40411d371f519df94419762051bdd38a1a1d8445a4b83ef3d6a9aa9572a | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
