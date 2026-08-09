# 🧬 Payload Analysis

`b4968b5c1402911c7871090bb8df1ecbafa84055c323a814c838667683e2773a`

## 📌 Resumen

Artefacto de 120 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.97. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b4968b5c1402911c7871090bb8df1ecbafa84055c323a814c838667683e2773a`
- **MD5:** `ffcb26cc0d0bb02d6ad68f685cf5f71a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 120 B |
| Entropía | 4.97 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.38.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 41.216.189.XXX | static_analysis |
| command | User-Agent: curl/7.38.0 | strings |
| hash | b4968b5c1402911c7871090bb8df1ecbafa84055c323a814c838667683e2773a | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
