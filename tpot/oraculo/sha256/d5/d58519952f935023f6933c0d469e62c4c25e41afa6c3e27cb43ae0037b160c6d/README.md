# 🧬 Payload Analysis

`d58519952f935023f6933c0d469e62c4c25e41afa6c3e27cb43ae0037b160c6d`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:46:01+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d58519952f935023f6933c0d469e62c4c25e41afa6c3e27cb43ae0037b160c6d`
- **SHA1:** `9d499578ad6efa93cd5d155dd16bf5c9c0716157`
- **MD5:** `cf84b20c0a9046d31975936735ebd7c2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 82 B |
| Entropía | 4.83 |
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
| ip | 190.179.163.XXX | static_analysis |
| hash | d58519952f935023f6933c0d469e62c4c25e41afa6c3e27cb43ae0037b160c6d | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| ip | 47.250.140.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
