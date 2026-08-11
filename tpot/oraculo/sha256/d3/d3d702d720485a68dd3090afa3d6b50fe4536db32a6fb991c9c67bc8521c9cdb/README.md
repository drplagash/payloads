# 🧬 Payload Analysis

`d3d702d720485a68dd3090afa3d6b50fe4536db32a6fb991c9c67bc8521c9cdb`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/d3d702d720485a68dd3090afa3d6b50fe4536db32a6fb991c9c67bc8521c9cdb.md](../../../../../malware-like/oraculo/botnet/d3d702d720485a68dd3090afa3d6b50fe4536db32a6fb991c9c67bc8521c9cdb.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d3d702d720485a68dd3090afa3d6b50fe4536db32a6fb991c9c67bc8521c9cdb`
- **SHA1:** `c4d5e025b4502fcf6552b35af24c5b3cca73a111`
- **MD5:** `bf3ccf08deb1eac6a592b5184b8980ec`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.92 |
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
| hash | d3d702d720485a68dd3090afa3d6b50fe4536db32a6fb991c9c67bc8521c9cdb | static_analysis |
| ip | 94.237.67.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
