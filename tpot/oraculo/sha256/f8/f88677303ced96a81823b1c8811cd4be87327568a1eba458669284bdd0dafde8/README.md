# 🧬 Payload Analysis

`f88677303ced96a81823b1c8811cd4be87327568a1eba458669284bdd0dafde8`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg2` en `hxxp://2.26.124.XXX/gg2`. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `2.26.124.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `94.154.43.XXX` — confianza Alto, evidencia hardcoded_in_payload Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/f88677303ced96a81823b1c8811cd4be87327568a1eba458669284bdd0dafde8.md](../../../../../malware-like/oraculo/downloader/f88677303ced96a81823b1c8811cd4be87327568a1eba458669284bdd0dafde8.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f88677303ced96a81823b1c8811cd4be87327568a1eba458669284bdd0dafde8`
- **SHA1:** `cf453c50b4cecebaf1842f41482d9045f8e8b7a4`
- **MD5:** `38190c8bd284fb31de90d977fb64d785`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (696), with CRLF line terminators |
| Tamaño | 1.6 KiB |
| Entropía | 5.43 |
| Strings | 24 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Comunicación remota**
3. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (696), with CRLF line terminators; iocs=6

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://2.26.124.XXX/gg2 | strings |
| url | hxxp://2.26.124.XXX/gg2) | strings |
| ip | 94.154.43.XXX | static_analysis |
| ip | 2.26.124.XXX | static_analysis |
| ip | 190.179.140.XXX | static_analysis |
| hash | f88677303ced96a81823b1c8811cd4be87327568a1eba458669284bdd0dafde8 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
