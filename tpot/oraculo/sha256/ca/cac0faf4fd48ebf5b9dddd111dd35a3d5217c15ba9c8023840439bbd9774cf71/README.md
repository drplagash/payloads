# 🧬 Payload Analysis

`cac0faf4fd48ebf5b9dddd111dd35a3d5217c15ba9c8023840439bbd9774cf71`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/cac0faf4fd48ebf5b9dddd111dd35a3d5217c15ba9c8023840439bbd9774cf71.md](../../../../../malware-like/oraculo/botnet/cac0faf4fd48ebf5b9dddd111dd35a3d5217c15ba9c8023840439bbd9774cf71.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:06:23.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cac0faf4fd48ebf5b9dddd111dd35a3d5217c15ba9c8023840439bbd9774cf71`
- **SHA1:** `16f7dd1e3968e0fcb7d03e79ee2c6fcdd06a477c`
- **MD5:** `6396a717be4a04438feebe5345de6570`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 88 B |
| Entropía | 4.72 |
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
| ip | 190.179.177.XXX | static_analysis |
| command | User-Agent: curl/7.61.1 | strings |
| hash | cac0faf4fd48ebf5b9dddd111dd35a3d5217c15ba9c8023840439bbd9774cf71 | static_analysis |
| ip | 103.123.226.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
