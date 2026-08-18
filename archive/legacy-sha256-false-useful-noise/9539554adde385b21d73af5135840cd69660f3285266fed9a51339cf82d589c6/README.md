# 🧬 Payload Analysis

`9539554adde385b21d73af5135840cd69660f3285266fed9a51339cf82d589c6`

## 📌 Resumen

Texto Unicode de 4.0 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `19` en `hxxp://www[.]w3[.]org/19`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/9539554adde385b21d73af5135840cd69660f3285266fed9a51339cf82d589c6.md](../../../../../malware-like/oraculo/downloader/9539554adde385b21d73af5135840cd69660f3285266fed9a51339cf82d589c6.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:22:20.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9539554adde385b21d73af5135840cd69660f3285266fed9a51339cf82d589c6`
- **SHA1:** `f0b177658c30a761a1af3d49f5b3c814b8bd4751`
- **MD5:** `a69a548296bf6e8c279901440da07d31`

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
| url | hxxp://www[.]w3[.]org/19 | strings |
| url | hxxp://www[.]w3[.]org/TR/xhtml1/DTD/xhtml1-transitional.dtd | strings |
| hash | 9539554adde385b21d73af5135840cd69660f3285266fed9a51339cf82d589c6 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
