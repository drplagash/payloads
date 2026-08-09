# 🧬 Payload Analysis

`6d58239e2080664d0832d06b2f4eb063fb081424a2d76d82eb8fc561bbdd2f47`

## 📌 Resumen

Artefacto de 113 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.95. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6d58239e2080664d0832d06b2f4eb063fb081424a2d76d82eb8fc561bbdd2f47`
- **SHA1:** `91e950afb8f1cc087a51ac2d59271bd2dcf3debb`
- **MD5:** `f1bb4c91c53f6bf4d55b75c5a25d98f6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 113 B |
| Entropía | 4.95 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.74.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| command | User-Agent: curl/7.74.0 | strings |
| hash | 6d58239e2080664d0832d06b2f4eb063fb081424a2d76d82eb8fc561bbdd2f47 | static_analysis |
| ip | 8.209.119.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
