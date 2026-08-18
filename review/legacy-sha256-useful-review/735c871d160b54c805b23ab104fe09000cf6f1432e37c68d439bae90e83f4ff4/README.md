# 🧬 Payload Analysis

`735c871d160b54c805b23ab104fe09000cf6f1432e37c68d439bae90e83f4ff4`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/735c871d160b54c805b23ab104fe09000cf6f1432e37c68d439bae90e83f4ff4.md](../../../../../malware-like/oraculo/botnet/735c871d160b54c805b23ab104fe09000cf6f1432e37c68d439bae90e83f4ff4.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:17:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `735c871d160b54c805b23ab104fe09000cf6f1432e37c68d439bae90e83f4ff4`
- **SHA1:** `adee161ee89b18c93b5dd7dc2b832e3900fd2d24`
- **MD5:** `de52075570a45a5bfe2647f4c4132195`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 710 B |
| Entropía | 5.19 |
| Strings | 30 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.73.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 94.156.152.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| hash | 735c871d160b54c805b23ab104fe09000cf6f1432e37c68d439bae90e83f4ff4 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
