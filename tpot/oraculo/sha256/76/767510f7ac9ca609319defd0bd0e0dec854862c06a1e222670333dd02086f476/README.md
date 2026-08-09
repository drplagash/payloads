# 🧬 Payload Analysis

`767510f7ac9ca609319defd0bd0e0dec854862c06a1e222670333dd02086f476`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:14+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `767510f7ac9ca609319defd0bd0e0dec854862c06a1e222670333dd02086f476`
- **SHA1:** `ec73caf82543a621baea8fef0df4f29d9e06f8a1`
- **MD5:** `4e168d2c1451b54dfcdc2b98f6f87c24`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 82 B |
| Entropía | 4.84 |
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
| ip | 190.179.144.XXX | static_analysis |
| hash | 767510f7ac9ca609319defd0bd0e0dec854862c06a1e222670333dd02086f476 | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| ip | 47.236.198.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
