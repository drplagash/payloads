# 🧬 Payload Analysis

`78a3b780c3a5d8aa89212cd844a2c72b420b110c22bdec00fb7fb846245235ac`

## 📌 Resumen

Artefacto de 84 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.87. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `78a3b780c3a5d8aa89212cd844a2c72b420b110c22bdec00fb7fb846245235ac`
- **SHA1:** `9d6b822b98718e8efce61e48d8c78ce80d05b6dc`
- **MD5:** `0bc626fa6e3c635735967b5010c542ed`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 84 B |
| Entropía | 4.87 |
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
| ip | 190.179.139.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 78a3b780c3a5d8aa89212cd844a2c72b420b110c22bdec00fb7fb846245235ac | static_analysis |
| ip | 47.84.191.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
