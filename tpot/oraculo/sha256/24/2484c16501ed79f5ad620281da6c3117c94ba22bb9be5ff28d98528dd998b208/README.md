# 🧬 Payload Analysis

`2484c16501ed79f5ad620281da6c3117c94ba22bb9be5ff28d98528dd998b208`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg10` en `hxxp://94.154.43.XXX/gg10`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/2484c16501ed79f5ad620281da6c3117c94ba22bb9be5ff28d98528dd998b208.md](../../../../../malware-like/oraculo/downloader/2484c16501ed79f5ad620281da6c3117c94ba22bb9be5ff28d98528dd998b208.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2484c16501ed79f5ad620281da6c3117c94ba22bb9be5ff28d98528dd998b208`
- **SHA1:** `8def6e8cbb30908a6b99dcb85bfb8373da379917`
- **MD5:** `99cb2c7395f82e0897602f91d8da66ef`

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
| ip | 190.179.139.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| hash | 2484c16501ed79f5ad620281da6c3117c94ba22bb9be5ff28d98528dd998b208 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
