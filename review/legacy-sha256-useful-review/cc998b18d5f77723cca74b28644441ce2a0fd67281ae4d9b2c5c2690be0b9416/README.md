# 🧬 Payload Analysis

`cc998b18d5f77723cca74b28644441ce2a0fd67281ae4d9b2c5c2690be0b9416`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificaron 2 comandos observados o extraídos. Se identificaron 4 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/cc998b18d5f77723cca74b28644441ce2a0fd67281ae4d9b2c5c2690be0b9416.md](../../../../../malware-like/oraculo/botnet/cc998b18d5f77723cca74b28644441ce2a0fd67281ae4d9b2c5c2690be0b9416.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:57:27.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cc998b18d5f77723cca74b28644441ce2a0fd67281ae4d9b2c5c2690be0b9416`
- **SHA1:** `a0d592bc93fae8d8ff515fc0453e0b2fd837b355`
- **MD5:** `201ebb91c4906f8154ebd9b59f2c7882`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 616 B |
| Entropía | 5.12 |
| Strings | 24 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
User-Agent: Wget/1.25.0 (linux-gnu)
User-Agent: curl/7.38.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 185.228.26.XXX | static_analysis |
| command | User-Agent: Wget/1.25.0 (linux-gnu) | strings |
| command | User-Agent: curl/7.38.0 | strings |
| hash | cc998b18d5f77723cca74b28644441ce2a0fd67281ae4d9b2c5c2690be0b9416 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
