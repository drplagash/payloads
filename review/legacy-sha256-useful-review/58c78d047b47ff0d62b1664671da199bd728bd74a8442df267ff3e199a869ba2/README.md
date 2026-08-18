# 🧬 Payload Analysis

`58c78d047b47ff0d62b1664671da199bd728bd74a8442df267ff3e199a869ba2`

## 📌 Resumen

Artefacto de 82 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.80. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:07:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `58c78d047b47ff0d62b1664671da199bd728bd74a8442df267ff3e199a869ba2`
- **SHA1:** `3b68c02196314c6d722cd7f7004c580c515d0515`
- **MD5:** `0904d9efb674047b1dff873555e713d7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 82 B |
| Entropía | 4.8 |
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
| ip | 190.179.172.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 58c78d047b47ff0d62b1664671da199bd728bd74a8442df267ff3e199a869ba2 | static_analysis |
| ip | 47.251.182.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
