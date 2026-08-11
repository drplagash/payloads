# 🧬 Payload Analysis

`bccab341eac82209eb099bc6e46592e6fae69599215bddde2172eeba53324a29`

## 📌 Resumen

Texto Unicode de 4.0 KiB. La evidencia disponible identifica capacidad de descarga remota. Infraestructura remota: `hxxp://www[.]w3[.]or`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/bccab341eac82209eb099bc6e46592e6fae69599215bddde2172eeba53324a29.md](../../../../../malware-like/oraculo/downloader/bccab341eac82209eb099bc6e46592e6fae69599215bddde2172eeba53324a29.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:58.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bccab341eac82209eb099bc6e46592e6fae69599215bddde2172eeba53324a29`
- **MD5:** `d348c76aef93132daa46ad277ebdc358`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | HTML document, Unicode text, UTF-8 text, with very long lines (1081), with CRLF, LF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.45 |
| Strings | 32 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=HTML document, Unicode text, UTF-8 text, with very long lines (1081), with CRLF, LF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]w3[.]or | strings |
| url | hxxp://www[.]w3[.]org/TR/xhtml1/DTD/xhtml1-transitional.dtd | strings |
| hash | bccab341eac82209eb099bc6e46592e6fae69599215bddde2172eeba53324a29 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
