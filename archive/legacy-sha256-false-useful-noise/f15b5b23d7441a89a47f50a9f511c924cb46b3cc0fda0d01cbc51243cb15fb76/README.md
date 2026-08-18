# 🧬 Payload Analysis

`f15b5b23d7441a89a47f50a9f511c924cb46b3cc0fda0d01cbc51243cb15fb76`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg10` en `hxxp://94.154.43.XXX/gg10`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/f15b5b23d7441a89a47f50a9f511c924cb46b3cc0fda0d01cbc51243cb15fb76.md](../../../../../malware-like/oraculo/downloader/f15b5b23d7441a89a47f50a9f511c924cb46b3cc0fda0d01cbc51243cb15fb76.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:37:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f15b5b23d7441a89a47f50a9f511c924cb46b3cc0fda0d01cbc51243cb15fb76`
- **MD5:** `fa994663e6046f51aeca732a93a5b1e9`

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
| ip | 190.179.174.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| hash | f15b5b23d7441a89a47f50a9f511c924cb46b3cc0fda0d01cbc51243cb15fb76 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
