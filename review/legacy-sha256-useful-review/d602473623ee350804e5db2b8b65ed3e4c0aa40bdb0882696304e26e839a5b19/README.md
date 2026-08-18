# 🧬 Payload Analysis

`d602473623ee350804e5db2b8b65ed3e4c0aa40bdb0882696304e26e839a5b19`

## 📌 Resumen

Artefacto de 111 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.93. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:09:36.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d602473623ee350804e5db2b8b65ed3e4c0aa40bdb0882696304e26e839a5b19`
- **SHA1:** `a2aaaef165b3d1c3bbcce351b5f79f81ac90f8b2`
- **MD5:** `5e2f006cef8cf303e8d23138feeb19d1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 111 B |
| Entropía | 4.93 |
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
| ip | 190.179.172.XXX | static_analysis |
| command | User-Agent: curl/7.74.0 | strings |
| hash | d602473623ee350804e5db2b8b65ed3e4c0aa40bdb0882696304e26e839a5b19 | static_analysis |
| ip | 47.251.30.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
