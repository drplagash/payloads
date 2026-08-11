# 🧬 Payload Analysis

`57c831c4f743091c112f02ac9180ff0ba99137490c0569b8741be51e31c5e9e7`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg` en `hxxp://2.26.124.XXX:99/gg`. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `2.26.124.XXX` — confianza Alto, evidencia hardcoded_in_payload Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/57c831c4f743091c112f02ac9180ff0ba99137490c0569b8741be51e31c5e9e7.md](../../../../../malware-like/oraculo/downloader/57c831c4f743091c112f02ac9180ff0ba99137490c0569b8741be51e31c5e9e7.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `57c831c4f743091c112f02ac9180ff0ba99137490c0569b8741be51e31c5e9e7`
- **SHA1:** `0d6a9051389a34330940ab12d590514e0129d136`
- **MD5:** `342ca033ca057e05c25e7244075c5f78`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (682), with CRLF line terminators |
| Tamaño | 1.6 KiB |
| Entropía | 5.42 |
| Strings | 24 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Comunicación remota**
3. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (682), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://2.26.124.XXX:99/gg) | strings |
| url | hxxp://2.26.124.XXX:99/gg | strings |
| ip | 2.26.124.XXX | static_analysis |
| ip | 190.179.140.XXX | static_analysis |
| hash | 57c831c4f743091c112f02ac9180ff0ba99137490c0569b8741be51e31c5e9e7 | static_analysis |
| ip | 94.154.43.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
