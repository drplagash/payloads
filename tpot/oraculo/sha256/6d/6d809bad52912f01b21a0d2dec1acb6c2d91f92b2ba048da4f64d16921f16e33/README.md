# 🧬 Payload Analysis

`6d809bad52912f01b21a0d2dec1acb6c2d91f92b2ba048da4f64d16921f16e33`

## 📌 Resumen

Artefacto de 98 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.00. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:40.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6d809bad52912f01b21a0d2dec1acb6c2d91f92b2ba048da4f64d16921f16e33`
- **SHA1:** `0be29b948b659e550bfbe7fbfe75ee72e6ce9eb1`
- **MD5:** `9c76d7de89e15487ce06bc3ab30bbc5c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 98 B |
| Entropía | 5 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.76.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| command | User-Agent: curl/7.76.1 | strings |
| hash | 6d809bad52912f01b21a0d2dec1acb6c2d91f92b2ba048da4f64d16921f16e33 | static_analysis |
| ip | 103.123.226.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
