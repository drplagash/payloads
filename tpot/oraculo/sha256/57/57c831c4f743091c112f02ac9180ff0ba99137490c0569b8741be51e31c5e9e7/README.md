# 🧬 Payload Analysis

`57c831c4f743091c112f02ac9180ff0ba99137490c0569b8741be51e31c5e9e7`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Comunicación remota, Cambio de permisos.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38+00:00`
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
| ip | 190.179.140.XXX | static_analysis |
| ip | 2.26.124.XXX | static_analysis |
| url | hxxp://2.26.124.XXX:99/gg | strings |
| url | hxxp://2.26.124.XXX:99/gg) | strings |
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
