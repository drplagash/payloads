# 🧬 Payload Analysis

`301793a9e9280e94c50c62f27539ec336e52eef8c8b9381693ce8bda263802a9`

## 📌 Resumen

Artefacto de 138 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.15. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:31:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `301793a9e9280e94c50c62f27539ec336e52eef8c8b9381693ce8bda263802a9`
- **MD5:** `ea9761477bcbce7cdf9bfe264c6f17f2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 138 B |
| Entropía | 5.15 |
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
| ip | 41.216.189.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| hash | 301793a9e9280e94c50c62f27539ec336e52eef8c8b9381693ce8bda263802a9 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
