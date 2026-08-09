# 🧬 Payload Analysis

`45f364ff2bde82ee6330dcc7a3f28e104193aeeec2ec16305246f81172e5ec2a`

## 📌 Resumen

Artefacto de 182 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.37. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:15:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `45f364ff2bde82ee6330dcc7a3f28e104193aeeec2ec16305246f81172e5ec2a`
- **SHA1:** `a0b7b90ee11d3c713c325df7877c1a28d18b5ee1`
- **MD5:** `0fd7b2916bd9e94b7a0a1dd63375b74f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 182 B |
| Entropía | 5.37 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: Wget/1.21.4 (HelpMeEscapeFromBelarus@proton.me)
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.153.XXX | static_analysis |
| command | User-Agent: Wget/1.21.4 (HelpMeEscapeFromBelarus@proton.me) | strings |
| hash | 45f364ff2bde82ee6330dcc7a3f28e104193aeeec2ec16305246f81172e5ec2a | static_analysis |
| ip | 124.164.251.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
