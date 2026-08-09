# 🧬 Payload Analysis

`6eb61b2f970581efae20f98b02f4fbc16f476ab45b79848a575300269e51dda1`

## 📌 Resumen

Artefacto de 87 B. Formato identificado como ASCII text. Entropía registrada: 4.94. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:00:23.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6eb61b2f970581efae20f98b02f4fbc16f476ab45b79848a575300269e51dda1`
- **SHA1:** `3ee1cc947537bf1999fc57602bb2826dec4ab8ac`
- **MD5:** `d7b5d6809db10933b2858e1248c4f525`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text |
| Tamaño | 87 B |
| Entropía | 4.94 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 6eb61b2f970581efae20f98b02f4fbc16f476ab45b79848a575300269e51dda1 | static_analysis |
| ip | 47.250.43.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
