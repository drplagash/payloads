# 🧬 Payload Analysis

`37dc4dcc5d258830c910afdde33cc98b4a96af0effb4c7e88a7ddc623c8fb2e0`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/37dc4dcc5d258830c910afdde33cc98b4a96af0effb4c7e88a7ddc623c8fb2e0.md](../../../../../malware-like/oraculo/botnet/37dc4dcc5d258830c910afdde33cc98b4a96af0effb4c7e88a7ddc623c8fb2e0.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `37dc4dcc5d258830c910afdde33cc98b4a96af0effb4c7e88a7ddc623c8fb2e0`
- **SHA1:** `6d101149a5c77024fd15e2ebc0c7eea72fd85367`
- **MD5:** `df49fdf0ea20a8d1d81a8874c7755bd7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.86 |
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
| hash | 37dc4dcc5d258830c910afdde33cc98b4a96af0effb4c7e88a7ddc623c8fb2e0 | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
