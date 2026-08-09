# 🧬 Payload Analysis

`86abffe114ed2a6356ba4bf30873d77546242cca2fcb73ee0f8e7e0f5717a7ba`

## 📌 Resumen

Artefacto de 435 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.16. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:24:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `86abffe114ed2a6356ba4bf30873d77546242cca2fcb73ee0f8e7e0f5717a7ba`
- **SHA1:** `4fce88bd21d650436c49617dc7eda470b64825d8`
- **MD5:** `7018fdff973883e1d683a8d893b0e268`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 435 B |
| Entropía | 5.16 |
| Strings | 18 |

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
| ip | 176.65.139.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| hash | 86abffe114ed2a6356ba4bf30873d77546242cca2fcb73ee0f8e7e0f5717a7ba | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
