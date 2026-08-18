# 🧬 Payload Analysis

`af928c6d71b1d88471f4a9b99ee34cce8c0945dc90ecb81d854e8618305227ab`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/af928c6d71b1d88471f4a9b99ee34cce8c0945dc90ecb81d854e8618305227ab.md](../../../../../malware-like/oraculo/botnet/af928c6d71b1d88471f4a9b99ee34cce8c0945dc90ecb81d854e8618305227ab.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `af928c6d71b1d88471f4a9b99ee34cce8c0945dc90ecb81d854e8618305227ab`
- **SHA1:** `f392e9e5933ff4f669b69ceebea9a3b6b32b097c`
- **MD5:** `6bd34f70fc41e33e7d4ce7ee8777f6e5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.9 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.68.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| command | User-Agent: curl/7.68.0 | strings |
| hash | af928c6d71b1d88471f4a9b99ee34cce8c0945dc90ecb81d854e8618305227ab | static_analysis |
| ip | 94.237.67.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
