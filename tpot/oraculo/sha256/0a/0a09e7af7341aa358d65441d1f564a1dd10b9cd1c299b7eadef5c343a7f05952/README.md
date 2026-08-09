# 🧬 Payload Analysis

`0a09e7af7341aa358d65441d1f564a1dd10b9cd1c299b7eadef5c343a7f05952`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (625), with CRLF line terminators de 804 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `envelope` en `hxxp://schemas[.]xmlsoap[.]org/soap/envelope/`. Se extrajeron 3 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0a09e7af7341aa358d65441d1f564a1dd10b9cd1c299b7eadef5c343a7f05952`
- **SHA1:** `7ce0a113769ad0cce8d039407338d2a6e9466409`
- **MD5:** `e3cd1869ce9ad6926132af299233c5b9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (625), with CRLF line terminators |
| Tamaño | 804 B |
| Entropía | 5.48 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (625), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://203.101.186.XXX:60296/Mozi.m | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| ip | 203.101.186.XXX | static_analysis |
| hash | 0a09e7af7341aa358d65441d1f564a1dd10b9cd1c299b7eadef5c343a7f05952 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
