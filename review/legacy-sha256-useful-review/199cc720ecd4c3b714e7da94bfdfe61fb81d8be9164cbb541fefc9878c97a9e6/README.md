# 🧬 Payload Analysis

`199cc720ecd4c3b714e7da94bfdfe61fb81d8be9164cbb541fefc9878c97a9e6`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/199cc720ecd4c3b714e7da94bfdfe61fb81d8be9164cbb541fefc9878c97a9e6.md](../../../../../malware-like/oraculo/botnet/199cc720ecd4c3b714e7da94bfdfe61fb81d8be9164cbb541fefc9878c97a9e6.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `199cc720ecd4c3b714e7da94bfdfe61fb81d8be9164cbb541fefc9878c97a9e6`
- **SHA1:** `cda0d3a0758d3e38a46a97435de37060760dd570`
- **MD5:** `f4c93a646c1e55da75c011215c77e344`

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
User-Agent: curl/7.61.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| command | User-Agent: curl/7.61.1 | strings |
| hash | 199cc720ecd4c3b714e7da94bfdfe61fb81d8be9164cbb541fefc9878c97a9e6 | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
