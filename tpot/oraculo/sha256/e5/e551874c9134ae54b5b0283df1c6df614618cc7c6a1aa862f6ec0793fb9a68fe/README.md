# 🧬 Payload Analysis

`e551874c9134ae54b5b0283df1c6df614618cc7c6a1aa862f6ec0793fb9a68fe`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e551874c9134ae54b5b0283df1c6df614618cc7c6a1aa862f6ec0793fb9a68fe`
- **SHA1:** `df1cc6e0afb2299a18534868c372e8d6307a60a5`
- **MD5:** `db155640718f460b581bd8eb0a31653c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 81 B |
| Entropía | 4.81 |
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
| ip | 190.179.160.XXX | static_analysis |
| hash | e551874c9134ae54b5b0283df1c6df614618cc7c6a1aa862f6ec0793fb9a68fe | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| ip | 8.219.106.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
