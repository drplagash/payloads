# 🧬 Payload Analysis

`f9ba01e33c671af8113bbf2b40ea08735867169cb7ab3e6219cdb3d2c47d0aa3`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/f9ba01e33c671af8113bbf2b40ea08735867169cb7ab3e6219cdb3d2c47d0aa3.md](../../../../../malware-like/oraculo/botnet/f9ba01e33c671af8113bbf2b40ea08735867169cb7ab3e6219cdb3d2c47d0aa3.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f9ba01e33c671af8113bbf2b40ea08735867169cb7ab3e6219cdb3d2c47d0aa3`
- **SHA1:** `af33b6e0e9dacf6f0f1976f51d6eebbd4b5bc15c`
- **MD5:** `1d3ddfe8fcee37ae3bd8e68be884b8cf`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.81 |
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
| hash | f9ba01e33c671af8113bbf2b40ea08735867169cb7ab3e6219cdb3d2c47d0aa3 | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
