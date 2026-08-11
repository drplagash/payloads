# 🧬 Payload Analysis

`cba814f435473e06a3cd46fedbd180bb2af8f362d79f04f7ca9d20f1dceb6eb7`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/cba814f435473e06a3cd46fedbd180bb2af8f362d79f04f7ca9d20f1dceb6eb7.md](../../../../../malware-like/oraculo/botnet/cba814f435473e06a3cd46fedbd180bb2af8f362d79f04f7ca9d20f1dceb6eb7.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:14.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cba814f435473e06a3cd46fedbd180bb2af8f362d79f04f7ca9d20f1dceb6eb7`
- **SHA1:** `b1c360a5bbdd6769b43084aab77c422142e2f254`
- **MD5:** `1164bae9fd9225bb8ba0b619a3dc3b86`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 86 B |
| Entropía | 4.83 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/8.5.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.144.XXX | static_analysis |
| command | User-Agent: curl/8.5.0 | strings |
| hash | cba814f435473e06a3cd46fedbd180bb2af8f362d79f04f7ca9d20f1dceb6eb7 | static_analysis |
| ip | 187.17.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
