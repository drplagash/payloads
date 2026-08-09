# 🧬 Payload Analysis

`ef813a2450a192a493ec66fbb23bfc7dbe6973fe48bf57b1b73d23960451c2f6`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ef813a2450a192a493ec66fbb23bfc7dbe6973fe48bf57b1b73d23960451c2f6`
- **SHA1:** `1bec9dbf8b93512bdeb48d2aeba44a2a00ea28cd`
- **MD5:** `7e99906bb358b93ab35241d60030aba5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 282 B |
| Entropía | 5.07 |
| Strings | 12 |

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
| ip | 93.115.101.XXX | static_analysis |
| hash | ef813a2450a192a493ec66fbb23bfc7dbe6973fe48bf57b1b73d23960451c2f6 | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
