# 🧬 Payload Analysis

`c5775af80dbb0aec6dd82b6b0b41a61f716ad1d637ba167bdb3ded73b4f5f49d`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:55+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c5775af80dbb0aec6dd82b6b0b41a61f716ad1d637ba167bdb3ded73b4f5f49d`
- **SHA1:** `3a5dc77a40b986a7755327d5f9b92ff583350a3b`
- **MD5:** `1a17c39ada5c54cbd0b0ac68ff75fb40`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.75 |
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
| hash | c5775af80dbb0aec6dd82b6b0b41a61f716ad1d637ba167bdb3ded73b4f5f49d | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| ip | 8.209.107.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
