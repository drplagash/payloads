# 🧬 Payload Analysis

`d04520fcbe4153822057c8eda9e526fa3fe1b0fb2dbae9d6f87eed5df6de3950`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/d04520fcbe4153822057c8eda9e526fa3fe1b0fb2dbae9d6f87eed5df6de3950.md](../../../../../malware-like/oraculo/botnet/d04520fcbe4153822057c8eda9e526fa3fe1b0fb2dbae9d6f87eed5df6de3950.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:40.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d04520fcbe4153822057c8eda9e526fa3fe1b0fb2dbae9d6f87eed5df6de3950`
- **SHA1:** `a44fcc6cedc92f4c853df7f57d78f6d3e61c0d4b`
- **MD5:** `6c9cb8ef30519887c6c912b9a582a3f2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 88 B |
| Entropía | 4.86 |
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
| ip | 190.179.169.XXX | static_analysis |
| command | User-Agent: curl/8.5.0 | strings |
| hash | d04520fcbe4153822057c8eda9e526fa3fe1b0fb2dbae9d6f87eed5df6de3950 | static_analysis |
| ip | 187.17.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
