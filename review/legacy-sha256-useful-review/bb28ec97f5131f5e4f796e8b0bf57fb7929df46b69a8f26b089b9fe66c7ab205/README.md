# 🧬 Payload Analysis

`bb28ec97f5131f5e4f796e8b0bf57fb7929df46b69a8f26b089b9fe66c7ab205`

## 📌 Resumen

Artefacto de 83 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.81. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:58:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bb28ec97f5131f5e4f796e8b0bf57fb7929df46b69a8f26b089b9fe66c7ab205`
- **SHA1:** `9cf047b35c507dfebb115f52163e1b3f926a735c`
- **MD5:** `fb17e6d3fde89fa693a88bc0f3227f03`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.81 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.160.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | bb28ec97f5131f5e4f796e8b0bf57fb7929df46b69a8f26b089b9fe66c7ab205 | static_analysis |
| ip | 47.251.104.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
