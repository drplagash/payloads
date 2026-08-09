# 🧬 Payload Analysis

`330c6f68847c5e1bd3bbc54c7ed620e50bdcccf3168f5308571836a59165332a`

## 📌 Resumen

Artefacto de 82 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.73. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:48:49.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `330c6f68847c5e1bd3bbc54c7ed620e50bdcccf3168f5308571836a59165332a`
- **SHA1:** `92e7ff2b9dcc1d7033c312aab59f5517186a9afa`
- **MD5:** `fbaee9b905648aa6bc598a02c1cd69c9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 82 B |
| Entropía | 4.73 |
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
| ip | 190.179.144.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 330c6f68847c5e1bd3bbc54c7ed620e50bdcccf3168f5308571836a59165332a | static_analysis |
| ip | 47.84.142.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
