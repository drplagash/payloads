# 🧬 Payload Analysis

`d4cb94027dcd137793b765fdd4ebc077781ec319347a98ac22c8802c9a17e4de`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Cambio de permisos, Descarga remota, Process killing, Temp directory use. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:24:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d4cb94027dcd137793b765fdd4ebc077781ec319347a98ac22c8802c9a17e4de`
- **SHA1:** `748242019ea7eee905a7ce45f1609c7afa401684`
- **MD5:** `9720b85b541c15889009bb526e537073`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JavaScript source, ASCII text, with very long lines (796), with CRLF line terminators |
| Tamaño | 1.7 KiB |
| Entropía | 5.44 |
| Strings | 24 |

## 🧠 Comportamiento observado

1. **Cambio de permisos**
2. **Descarga remota**
3. **Process killing**
4. **Temp directory use**
5. **Comunicación remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JavaScript source, ASCII text, with very long lines (796), with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX:67/sonnet.x86 | strings |
| ip | 190.179.128.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| hash | d4cb94027dcd137793b765fdd4ebc077781ec319347a98ac22c8802c9a17e4de | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
