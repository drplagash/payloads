# 🧬 Payload Analysis

`bc319a5ea7f37a8c892ec8fe09f53ce979f980c0ca2e04fed17aa3cbbf9f7c8b`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/bc319a5ea7f37a8c892ec8fe09f53ce979f980c0ca2e04fed17aa3cbbf9f7c8b.md](../../../../../malware-like/oraculo/botnet/bc319a5ea7f37a8c892ec8fe09f53ce979f980c0ca2e04fed17aa3cbbf9f7c8b.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bc319a5ea7f37a8c892ec8fe09f53ce979f980c0ca2e04fed17aa3cbbf9f7c8b`
- **SHA1:** `20ec6b259239499ce4fb7a4c060ad715b4ddb778`
- **MD5:** `5c768c02858da7d89c85d5fdf32ac8bb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.84 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.61.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| command | User-Agent: curl/7.61.1 | strings |
| hash | bc319a5ea7f37a8c892ec8fe09f53ce979f980c0ca2e04fed17aa3cbbf9f7c8b | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
