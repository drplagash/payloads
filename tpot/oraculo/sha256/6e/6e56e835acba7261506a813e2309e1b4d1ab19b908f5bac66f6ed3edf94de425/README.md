# 🧬 Payload Analysis

`6e56e835acba7261506a813e2309e1b4d1ab19b908f5bac66f6ed3edf94de425`

## 📌 Resumen

Artefacto identificado como HTML document, Unicode text, UTF-8 text, with CRLF, LF line terminators de 4.0 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `css` en `hxxps://fonts[.]googleapis[.]com/css`. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6e56e835acba7261506a813e2309e1b4d1ab19b908f5bac66f6ed3edf94de425`
- **SHA1:** `b61f7d5c885605027be6155edc4c692c5a8a570f`
- **MD5:** `9a5670bd5dc71c22f73d3645768ad988`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | HTML document, Unicode text, UTF-8 text, with CRLF, LF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.1 |
| Strings | 115 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=HTML document, Unicode text, UTF-8 text, with CRLF, LF line terminators; strings=115; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://fonts[.]googleapis[.]com/css?family=Open+Sans | strings |
| hash | 6e56e835acba7261506a813e2309e1b4d1ab19b908f5bac66f6ed3edf94de425 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
