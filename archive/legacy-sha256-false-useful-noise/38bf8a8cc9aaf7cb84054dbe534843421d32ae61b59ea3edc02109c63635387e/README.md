# 🧬 Payload Analysis

`38bf8a8cc9aaf7cb84054dbe534843421d32ae61b59ea3edc02109c63635387e`

## 📌 Resumen

Texto Unicode de 4.0 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `css` en `hxxps://fonts[.]googleapis[.]com/css`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/38bf8a8cc9aaf7cb84054dbe534843421d32ae61b59ea3edc02109c63635387e.md](../../../../../malware-like/oraculo/downloader/38bf8a8cc9aaf7cb84054dbe534843421d32ae61b59ea3edc02109c63635387e.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `38bf8a8cc9aaf7cb84054dbe534843421d32ae61b59ea3edc02109c63635387e`
- **SHA1:** `d5347eec329c40644d082b4db3900979dd43afcb`
- **MD5:** `34a36ed433e9b2b93cabc5b7849cdaed`

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
| hash | 38bf8a8cc9aaf7cb84054dbe534843421d32ae61b59ea3edc02109c63635387e | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
