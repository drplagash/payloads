# 🧬 Payload Analysis

`2854954a414d0ac5e44c8145d830d38c6dc0ef58c1f9518d26b8eb7f76ea58b3`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/2854954a414d0ac5e44c8145d830d38c6dc0ef58c1f9518d26b8eb7f76ea58b3.md](../../../../../malware-like/oraculo/botnet/2854954a414d0ac5e44c8145d830d38c6dc0ef58c1f9518d26b8eb7f76ea58b3.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2854954a414d0ac5e44c8145d830d38c6dc0ef58c1f9518d26b8eb7f76ea58b3`
- **SHA1:** `bcbdd47bb7fe6ced900d350c77537ec3cd9df2a7`
- **MD5:** `9bc548c25dc7072b9d432879e1cb2d96`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.76 |
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
| hash | 2854954a414d0ac5e44c8145d830d38c6dc0ef58c1f9518d26b8eb7f76ea58b3 | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
