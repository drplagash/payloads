# 🧬 Payload Analysis

`6b6b0e05d936522fcb72d885d3bcb7d05b8192bbc71625fb8be20d9a136b5ebc`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg10` en `hxxp://94.154.43.XXX/gg10`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/6b6b0e05d936522fcb72d885d3bcb7d05b8192bbc71625fb8be20d9a136b5ebc.md](../../../../../malware-like/oraculo/downloader/6b6b0e05d936522fcb72d885d3bcb7d05b8192bbc71625fb8be20d9a136b5ebc.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6b6b0e05d936522fcb72d885d3bcb7d05b8192bbc71625fb8be20d9a136b5ebc`
- **MD5:** `9e587a4b921f3caec4d939a892a2d1ae`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (698), with CRLF line terminators |
| Tamaño | 1.6 KiB |
| Entropía | 5.44 |
| Strings | 24 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (698), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/gg10 | strings |
| url | hxxp://94.154.43.XXX/gg10) | strings |
| ip | 94.154.43.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| hash | 6b6b0e05d936522fcb72d885d3bcb7d05b8192bbc71625fb8be20d9a136b5ebc | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
