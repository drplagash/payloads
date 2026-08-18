# 🧬 Payload Analysis

`394ab9d6815b92fa81dbdad8a5cc5b57812d342a658df6b0b0b482e19de7af89`

## 📌 Resumen

Texto Unicode de 4.0 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `css` en `hxxps://fonts[.]googleapis[.]com/css`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/394ab9d6815b92fa81dbdad8a5cc5b57812d342a658df6b0b0b482e19de7af89.md](../../../../../malware-like/oraculo/downloader/394ab9d6815b92fa81dbdad8a5cc5b57812d342a658df6b0b0b482e19de7af89.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `394ab9d6815b92fa81dbdad8a5cc5b57812d342a658df6b0b0b482e19de7af89`
- **SHA1:** `68bd252959097c3cef66825647debd8b629dac87`
- **MD5:** `a2925398b39eb57c0e8972c2b77d8046`

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
| hash | 394ab9d6815b92fa81dbdad8a5cc5b57812d342a658df6b0b0b482e19de7af89 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
