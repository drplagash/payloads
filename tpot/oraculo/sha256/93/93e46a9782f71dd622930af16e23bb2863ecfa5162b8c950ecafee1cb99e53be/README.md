# 🧬 Payload Analysis

`93e46a9782f71dd622930af16e23bb2863ecfa5162b8c950ecafee1cb99e53be`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 312 B. La evidencia estática disponible identifica capacidad de descarga remota. Se observaron o extrajeron 3 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:16.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `93e46a9782f71dd622930af16e23bb2863ecfa5162b8c950ecafee1cb99e53be`
- **SHA1:** `5e58d43ef9bad10852c9ac689a19c08b3221013c`
- **MD5:** `582ec94b674c7e31f7a8df53f3830706`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 312 B |
| Entropía | 5.21 |
| Strings | 12 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /rondo.bmv.sh%7C%7Cwget HTTP/1.1
User-Agent: curl/7.73.0
GET /rondo.bmv.sh%7C%7Ccurl HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 204.10.194.XXX | static_analysis |
| command | GET /rondo.bmv.sh%7C%7Cwget HTTP/1.1 | strings |
| command | User-Agent: curl/7.73.0 | strings |
| command | GET /rondo.bmv.sh%7C%7Ccurl HTTP/1.1 | strings |
| hash | 93e46a9782f71dd622930af16e23bb2863ecfa5162b8c950ecafee1cb99e53be | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
