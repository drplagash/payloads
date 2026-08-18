# 🧬 Payload Analysis

`fb63e9e45521f452cb9985362931c1d7284f71200f075f723775822a3fa53646`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg10` en `hxxp://94.154.43.XXX/gg10`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/fb63e9e45521f452cb9985362931c1d7284f71200f075f723775822a3fa53646.md](../../../../../malware-like/oraculo/downloader/fb63e9e45521f452cb9985362931c1d7284f71200f075f723775822a3fa53646.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fb63e9e45521f452cb9985362931c1d7284f71200f075f723775822a3fa53646`
- **MD5:** `85cfebaa46b170866aaf067bfcb7d3d2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (698), with CRLF line terminators |
| Tamaño | 1.6 KiB |
| Entropía | 5.44 |
| Strings | 24 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/gg10) | strings |
| url | hxxp://94.154.43.XXX/gg10 | strings |
| ip | 94.154.43.XXX | static_analysis |
| ip | 190.179.177.XXX | static_analysis |
| hash | fb63e9e45521f452cb9985362931c1d7284f71200f075f723775822a3fa53646 | static_analysis |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_Shell_Script |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
