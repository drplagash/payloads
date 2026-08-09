# 🧬 Payload Analysis

`e7dd94d3db5b2b52eb22c182b8d78b9fcef9909a51a8a9421ac5bed36d91ad52`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:39:05+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e7dd94d3db5b2b52eb22c182b8d78b9fcef9909a51a8a9421ac5bed36d91ad52`
- **SHA1:** `e50efc1db0af3a6ac2df755c774d79b1cfe220e8`
- **MD5:** `18743fb3d5c4b032cd3a90cc9e23791b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 84 B |
| Entropía | 4.73 |
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
| ip | 190.179.166.XXX | static_analysis |
| hash | e7dd94d3db5b2b52eb22c182b8d78b9fcef9909a51a8a9421ac5bed36d91ad52 | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| ip | 47.254.152.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
