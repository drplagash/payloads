# 🧬 Payload Analysis

`856b4c7275c3aea609bc74b0b97903c889521bec404fccd05755f18d6c3c05c1`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg` en `hxxp://2.26.124.XXX:99/gg`. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `2.26.124.XXX` — confianza Alto, evidencia hardcoded_in_payload Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/856b4c7275c3aea609bc74b0b97903c889521bec404fccd05755f18d6c3c05c1.md](../../../../../malware-like/oraculo/downloader/856b4c7275c3aea609bc74b0b97903c889521bec404fccd05755f18d6c3c05c1.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `856b4c7275c3aea609bc74b0b97903c889521bec404fccd05755f18d6c3c05c1`
- **SHA1:** `31213cf92b5125617675589e18855f9e94cb874a`
- **MD5:** `e4192e992f7ae5fe54dcde802862d29d`

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
| hash | 856b4c7275c3aea609bc74b0b97903c889521bec404fccd05755f18d6c3c05c1 | static_analysis |
| ip | 94.154.43.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
