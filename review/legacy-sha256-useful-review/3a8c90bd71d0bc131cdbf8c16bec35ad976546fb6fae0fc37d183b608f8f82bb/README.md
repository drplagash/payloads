# 🧬 Payload Analysis

`3a8c90bd71d0bc131cdbf8c16bec35ad976546fb6fae0fc37d183b608f8f82bb`

## 📌 Resumen

Artefacto de 96 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.91. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:44:03.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3a8c90bd71d0bc131cdbf8c16bec35ad976546fb6fae0fc37d183b608f8f82bb`
- **MD5:** `900174edafb8d14bd822b2634f511dfd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 96 B |
| Entropía | 4.91 |
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
| ip | 190.179.168.XXX | static_analysis |
| command | User-Agent: curl/7.81.0 | strings |
| hash | 3a8c90bd71d0bc131cdbf8c16bec35ad976546fb6fae0fc37d183b608f8f82bb | static_analysis |
| ip | 136.113.171.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
