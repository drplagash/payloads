# 🧬 Payload Analysis

`b4eea6f1792fed4398ee6c7f8df478c4d64c7ffd6d5b1e2f7be20a8892a67f38`

## 📌 Resumen

Artefacto de 558 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.09. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Ejecución. Se identificaron 2 comandos observados o extraídos. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:31:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b4eea6f1792fed4398ee6c7f8df478c4d64c7ffd6d5b1e2f7be20a8892a67f38`
- **MD5:** `384deaeae05efd5b3fa8cc3f2828f88f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 558 B |
| Entropía | 5.09 |
| Strings | 24 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.73.0
GET /wget.sh HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 45.130.151.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| command | GET /wget.sh HTTP/1.1 | strings |
| hash | b4eea6f1792fed4398ee6c7f8df478c4d64c7ffd6d5b1e2f7be20a8892a67f38 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
