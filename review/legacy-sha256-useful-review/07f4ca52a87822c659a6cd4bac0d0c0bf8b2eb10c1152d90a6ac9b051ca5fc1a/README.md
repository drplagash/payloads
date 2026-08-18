# 🧬 Payload Analysis

`07f4ca52a87822c659a6cd4bac0d0c0bf8b2eb10c1152d90a6ac9b051ca5fc1a`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/07f4ca52a87822c659a6cd4bac0d0c0bf8b2eb10c1152d90a6ac9b051ca5fc1a.md](../../../../../malware-like/oraculo/botnet/07f4ca52a87822c659a6cd4bac0d0c0bf8b2eb10c1152d90a6ac9b051ca5fc1a.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `07f4ca52a87822c659a6cd4bac0d0c0bf8b2eb10c1152d90a6ac9b051ca5fc1a`
- **SHA1:** `e79656f8238cd6d3e5a7212fc240defe8721da7c`
- **MD5:** `c517791176c307e517a50cdd79543224`

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
| hash | 07f4ca52a87822c659a6cd4bac0d0c0bf8b2eb10c1152d90a6ac9b051ca5fc1a | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
