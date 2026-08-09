# 🧬 Payload Analysis

`307be4bad7b5b8bd129d98feda87b0bfa06d6b0f7f4dc5457e15d61faf7e65c9`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `307be4bad7b5b8bd129d98feda87b0bfa06d6b0f7f4dc5457e15d61faf7e65c9`
- **SHA1:** `2975e139ce2450a8e06e99fee17d6c7c556454e7`
- **MD5:** `5c269efd6eb66d13d0c31dfd696e32ae`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 84 B |
| Entropía | 4.76 |
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
| ip | 190.179.169.XXX | static_analysis |
| hash | 307be4bad7b5b8bd129d98feda87b0bfa06d6b0f7f4dc5457e15d61faf7e65c9 | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| ip | 47.251.20.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
