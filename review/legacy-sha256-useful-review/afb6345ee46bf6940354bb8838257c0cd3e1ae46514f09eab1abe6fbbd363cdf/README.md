# 🧬 Payload Analysis

`afb6345ee46bf6940354bb8838257c0cd3e1ae46514f09eab1abe6fbbd363cdf`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/afb6345ee46bf6940354bb8838257c0cd3e1ae46514f09eab1abe6fbbd363cdf.md](../../../../../malware-like/oraculo/botnet/afb6345ee46bf6940354bb8838257c0cd3e1ae46514f09eab1abe6fbbd363cdf.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `afb6345ee46bf6940354bb8838257c0cd3e1ae46514f09eab1abe6fbbd363cdf`
- **SHA1:** `c1bf1145783c621e95a949ca35ae77be3a0ee6e2`
- **MD5:** `1b3170a55ccb5b1728bff9cf1fd2d673`

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
| hash | afb6345ee46bf6940354bb8838257c0cd3e1ae46514f09eab1abe6fbbd363cdf | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
