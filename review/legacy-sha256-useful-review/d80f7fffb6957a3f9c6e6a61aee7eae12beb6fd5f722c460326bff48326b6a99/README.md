# 🧬 Payload Analysis

`d80f7fffb6957a3f9c6e6a61aee7eae12beb6fd5f722c460326bff48326b6a99`

## 📌 Resumen

Artefacto de 111 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.93. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:36:13.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d80f7fffb6957a3f9c6e6a61aee7eae12beb6fd5f722c460326bff48326b6a99`
- **MD5:** `288613045171c26256a648d371d222dc`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 111 B |
| Entropía | 4.93 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.74.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.174.XXX | static_analysis |
| command | User-Agent: curl/7.74.0 | strings |
| hash | d80f7fffb6957a3f9c6e6a61aee7eae12beb6fd5f722c460326bff48326b6a99 | static_analysis |
| ip | 47.254.184.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
