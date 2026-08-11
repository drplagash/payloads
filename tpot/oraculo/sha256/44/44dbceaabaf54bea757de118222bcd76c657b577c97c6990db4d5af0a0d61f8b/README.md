# 🧬 Payload Analysis

`44dbceaabaf54bea757de118222bcd76c657b577c97c6990db4d5af0a0d61f8b`

## 📌 Resumen

Script JavaScript de 1.6 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gg2` en `hxxp://94.154.43.XXX/gg2`. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.168.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `94.154.43.XXX` — confianza Alto, evidencia hardcoded_in_payload Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/44dbceaabaf54bea757de118222bcd76c657b577c97c6990db4d5af0a0d61f8b.md](../../../../../malware-like/oraculo/downloader/44dbceaabaf54bea757de118222bcd76c657b577c97c6990db4d5af0a0d61f8b.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `44dbceaabaf54bea757de118222bcd76c657b577c97c6990db4d5af0a0d61f8b`
- **SHA1:** `3303e8bb9784f96695bc724f44e3d766e4eb4b95`
- **MD5:** `6e9fe4c2aa33e59bfa26a163fc83a0e3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (696), with CRLF line terminators |
| Tamaño | 1.6 KiB |
| Entropía | 5.44 |
| Strings | 24 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Comunicación remota**
3. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (696), with CRLF line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/gg2) | strings |
| url | hxxp://94.154.43.XXX/gg2 | strings |
| ip | 94.154.43.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 44dbceaabaf54bea757de118222bcd76c657b577c97c6990db4d5af0a0d61f8b | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
