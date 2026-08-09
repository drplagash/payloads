# 🧬 Payload Analysis

`da004f5579606c3c6dee4c1d808cce24222c68ef4dce454061c85446cfd78b63`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Cambio de permisos, Descarga remota, Process killing, Temp directory use.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:24:17+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `da004f5579606c3c6dee4c1d808cce24222c68ef4dce454061c85446cfd78b63`
- **SHA1:** `e0f8ec7ad561296765e4dd5973652d18151c2fae`
- **MD5:** `380496372dcb242a67b0f8b590a23929`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (796), with CRLF line terminators |
| Tamaño | 1.4 KiB |
| Entropía | 5.37 |
| Strings | 15 |

## 🧠 Comportamiento observado

1. **Cambio de permisos**
2. **Descarga remota**
3. **Process killing**
4. **Temp directory use**
5. **Comunicación remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (796), with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX:67/sonnet.x86 | strings |
| hash | da004f5579606c3c6dee4c1d808cce24222c68ef4dce454061c85446cfd78b63 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
