# 🧬 Payload Analysis

`c2b2b36e3cbb9ee58ff26113495e74f2641c6e676af7de6131c58d1cb8b3c5e3`

## 📌 Resumen

Artefacto de 81 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.72. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c2b2b36e3cbb9ee58ff26113495e74f2641c6e676af7de6131c58d1cb8b3c5e3`
- **SHA1:** `ebda3917cb25e5552f348c1c420621a9be4d467c`
- **MD5:** `d1ff9de1bbb4959e6a6bdc1817b796bc`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 81 B |
| Entropía | 4.72 |
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
| ip | 190.179.177.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | c2b2b36e3cbb9ee58ff26113495e74f2641c6e676af7de6131c58d1cb8b3c5e3 | static_analysis |
| ip | 47.251.122.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
