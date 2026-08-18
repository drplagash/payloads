# 🧬 Payload Analysis

`a8c100e5eb03ad034de023d8efd0c3dbabbdb477cedf751a6d2982f0c52d100c`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/a8c100e5eb03ad034de023d8efd0c3dbabbdb477cedf751a6d2982f0c52d100c.md](../../../../../malware-like/oraculo/botnet/a8c100e5eb03ad034de023d8efd0c3dbabbdb477cedf751a6d2982f0c52d100c.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a8c100e5eb03ad034de023d8efd0c3dbabbdb477cedf751a6d2982f0c52d100c`
- **SHA1:** `f320488ca14b66e561fe2cce84c414f4ded29465`
- **MD5:** `aefbe72d6ed6912179a6258ceb274186`

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
| hash | a8c100e5eb03ad034de023d8efd0c3dbabbdb477cedf751a6d2982f0c52d100c | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
