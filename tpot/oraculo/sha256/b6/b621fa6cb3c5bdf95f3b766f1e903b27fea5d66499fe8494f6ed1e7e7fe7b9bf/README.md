# 🧬 Payload Analysis

`b621fa6cb3c5bdf95f3b766f1e903b27fea5d66499fe8494f6ed1e7e7fe7b9bf`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia disponible identifica capacidad de descarga remota. Infraestructura remota: `hxxps://return[.]st/`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/b621fa6cb3c5bdf95f3b766f1e903b27fea5d66499fe8494f6ed1e7e7fe7b9bf.md](../../../../../malware-like/oraculo/downloader/b621fa6cb3c5bdf95f3b766f1e903b27fea5d66499fe8494f6ed1e7e7fe7b9bf.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:43:29.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b621fa6cb3c5bdf95f3b766f1e903b27fea5d66499fe8494f6ed1e7e7fe7b9bf`
- **MD5:** `9e57039b2268380f284f407ec46099b2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (906), with CRLF line terminators |
| Tamaño | 1.6 KiB |
| Entropía | 5.76 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (906), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://return[.]st/?ref=Q7hw1uZ6pEz8LTEX | strings |
| url | hxxp://ip/x86; | strings |
| url | hxxps://return[.]st/?ref=Q7hw1uZ6pEz8LTEX;307; | strings |
| ip | 190.179.168.XXX | static_analysis |
| hash | b621fa6cb3c5bdf95f3b766f1e903b27fea5d66499fe8494f6ed1e7e7fe7b9bf | static_analysis |
| ip | 31.59.160.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
