# 🧬 Payload Analysis

`cdd819226d424e2f32075fc1dd009c258b37cb2e96e627985da29ec1177274c2`

## 📌 Resumen

Artefacto de 834 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.07. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Ejecución. Se identificaron 2 comandos observados o extraídos. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:35:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cdd819226d424e2f32075fc1dd009c258b37cb2e96e627985da29ec1177274c2`
- **MD5:** `1bfcf327e5a5c9893bbf2843fd536900`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 834 B |
| Entropía | 5.07 |
| Strings | 36 |

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
| ip | 31.77.227.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| command | GET /wget.sh HTTP/1.1 | strings |
| hash | cdd819226d424e2f32075fc1dd009c258b37cb2e96e627985da29ec1177274c2 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
