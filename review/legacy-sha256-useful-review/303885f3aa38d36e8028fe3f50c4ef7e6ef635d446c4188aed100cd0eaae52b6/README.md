# 🧬 Payload Analysis

`303885f3aa38d36e8028fe3f50c4ef7e6ef635d446c4188aed100cd0eaae52b6`

## 📌 Resumen

Artefacto de 79 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.74. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:47:25.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `303885f3aa38d36e8028fe3f50c4ef7e6ef635d446c4188aed100cd0eaae52b6`
- **SHA1:** `3f912b94e3c74f3040673105eacd0165f00abf5d`
- **MD5:** `6d5000b9cf75a8b39d46cb3131eefcbd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 79 B |
| Entropía | 4.74 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.78.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.144.XXX | static_analysis |
| command | User-Agent: curl/7.78.0 | strings |
| hash | 303885f3aa38d36e8028fe3f50c4ef7e6ef635d446c4188aed100cd0eaae52b6 | static_analysis |
| ip | 47.74.33.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
