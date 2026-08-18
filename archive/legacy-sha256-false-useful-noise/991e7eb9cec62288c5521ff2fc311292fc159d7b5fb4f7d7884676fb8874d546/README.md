# 🧬 Payload Analysis

`991e7eb9cec62288c5521ff2fc311292fc159d7b5fb4f7d7884676fb8874d546`

## 📌 Resumen

Texto Unicode de 3.1 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `css` en `hxxps://fonts[.]googleapis[.]com/css`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/991e7eb9cec62288c5521ff2fc311292fc159d7b5fb4f7d7884676fb8874d546.md](../../../../../malware-like/oraculo/downloader/991e7eb9cec62288c5521ff2fc311292fc159d7b5fb4f7d7884676fb8874d546.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `991e7eb9cec62288c5521ff2fc311292fc159d7b5fb4f7d7884676fb8874d546`
- **SHA1:** `67a8249fc9a4e375837bfb5681c8c2e1ebc009d7`
- **MD5:** `97db6e63a69203a314f4ed8a8cd6eb33`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | HTML document, Unicode text, UTF-8 text, with CRLF, LF line terminators |
| Tamaño | 3.1 KiB |
| Entropía | 5.1 |
| Strings | 87 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=HTML document, Unicode text, UTF-8 text, with CRLF, LF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://fonts[.]googleapis[.]com/css?family=Open+Sans | strings |
| hash | 991e7eb9cec62288c5521ff2fc311292fc159d7b5fb4f7d7884676fb8874d546 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
