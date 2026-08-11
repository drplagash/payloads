# 🧬 Payload Analysis

`9f2f65bce3847e36d9e8f490cefc70fba526822b57819f54f70d9104f86bb1fb`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/9f2f65bce3847e36d9e8f490cefc70fba526822b57819f54f70d9104f86bb1fb.md](../../../../../malware-like/oraculo/botnet/9f2f65bce3847e36d9e8f490cefc70fba526822b57819f54f70d9104f86bb1fb.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9f2f65bce3847e36d9e8f490cefc70fba526822b57819f54f70d9104f86bb1fb`
- **SHA1:** `134ad40fe8695028d3b5c2b0e3b8de42234511ab`
- **MD5:** `f29418e09ddffaabe99a87f74795b6c1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.82 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.88.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| command | User-Agent: curl/7.88.1 | strings |
| hash | 9f2f65bce3847e36d9e8f490cefc70fba526822b57819f54f70d9104f86bb1fb | static_analysis |
| ip | 191.242.209.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
