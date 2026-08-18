# 🧬 Payload Analysis

`3c2f31bcac44c8e0bca65a57c2791ad2b952324395cd2d2be6f8b907103c5297`

## 📌 Resumen

Artefacto de 83 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.79. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3c2f31bcac44c8e0bca65a57c2791ad2b952324395cd2d2be6f8b907103c5297`
- **SHA1:** `0a9aedbd5e1680fe8ad38ad29f42d505bfb6e9e1`
- **MD5:** `024291fd042e19ab6d6a1f2c1f584f39`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.79 |
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
| ip | 190.179.140.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 3c2f31bcac44c8e0bca65a57c2791ad2b952324395cd2d2be6f8b907103c5297 | static_analysis |
| ip | 47.251.179.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
