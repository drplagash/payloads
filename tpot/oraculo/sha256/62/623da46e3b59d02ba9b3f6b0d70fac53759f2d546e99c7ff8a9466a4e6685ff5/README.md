# 🧬 Payload Analysis

`623da46e3b59d02ba9b3f6b0d70fac53759f2d546e99c7ff8a9466a4e6685ff5`

## 📌 Resumen

Artefacto de 144 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.14. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:16.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `623da46e3b59d02ba9b3f6b0d70fac53759f2d546e99c7ff8a9466a4e6685ff5`
- **SHA1:** `d286a3dbc48e28ea2993da239eedc4a165bbe458`
- **MD5:** `a380cb12c36b2824488777a1fe5c7453`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 144 B |
| Entropía | 5.14 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.73.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 152.89.76.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| hash | 623da46e3b59d02ba9b3f6b0d70fac53759f2d546e99c7ff8a9466a4e6685ff5 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
