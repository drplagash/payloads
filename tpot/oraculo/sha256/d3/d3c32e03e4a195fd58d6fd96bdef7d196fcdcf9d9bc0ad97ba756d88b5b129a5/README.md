# 🧬 Payload Analysis

`d3c32e03e4a195fd58d6fd96bdef7d196fcdcf9d9bc0ad97ba756d88b5b129a5`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/d3c32e03e4a195fd58d6fd96bdef7d196fcdcf9d9bc0ad97ba756d88b5b129a5.md](../../../../../malware-like/oraculo/botnet/d3c32e03e4a195fd58d6fd96bdef7d196fcdcf9d9bc0ad97ba756d88b5b129a5.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d3c32e03e4a195fd58d6fd96bdef7d196fcdcf9d9bc0ad97ba756d88b5b129a5`
- **SHA1:** `47e6b695d2f5a6c6602e30ab97034449d3c4ba71`
- **MD5:** `d0716915d10277d6dd104bd9dad7fd26`

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
| hash | d3c32e03e4a195fd58d6fd96bdef7d196fcdcf9d9bc0ad97ba756d88b5b129a5 | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
