# 🧬 Payload Analysis

`e78c3af5a4c7414ddd73f5435a56f1de788675293d58f0ea2d3ad89f414d999d`

## 📌 Resumen

Artefacto de 86 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.88. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:25.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e78c3af5a4c7414ddd73f5435a56f1de788675293d58f0ea2d3ad89f414d999d`
- **MD5:** `94e9413972985b83a7810b9c7396a1a4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 86 B |
| Entropía | 4.88 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.81.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.175.XXX | static_analysis |
| command | User-Agent: curl/7.81.0 | strings |
| hash | e78c3af5a4c7414ddd73f5435a56f1de788675293d58f0ea2d3ad89f414d999d | static_analysis |
| ip | 172.110.223.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
