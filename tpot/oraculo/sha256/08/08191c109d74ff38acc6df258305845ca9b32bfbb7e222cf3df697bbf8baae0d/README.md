# 🧬 Payload Analysis

`08191c109d74ff38acc6df258305845ca9b32bfbb7e222cf3df697bbf8baae0d`

## 📌 Resumen

Artefacto de 139 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.17. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `08191c109d74ff38acc6df258305845ca9b32bfbb7e222cf3df697bbf8baae0d`
- **SHA1:** `7ba8b008e9d024033fea8cb15b787f7e4800d522`
- **MD5:** `769d52684bae7848987f747e29fce5be`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 139 B |
| Entropía | 5.17 |
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
| hash | 08191c109d74ff38acc6df258305845ca9b32bfbb7e222cf3df697bbf8baae0d | static_analysis |
| ip | 103.123.226.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
