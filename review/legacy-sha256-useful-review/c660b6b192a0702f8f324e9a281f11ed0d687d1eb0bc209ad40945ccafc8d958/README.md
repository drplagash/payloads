# 🧬 Payload Analysis

`c660b6b192a0702f8f324e9a281f11ed0d687d1eb0bc209ad40945ccafc8d958`

## 📌 Resumen

Artefacto de 87 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.90. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:25.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c660b6b192a0702f8f324e9a281f11ed0d687d1eb0bc209ad40945ccafc8d958`
- **MD5:** `6e184b3771431f51ae0bdc59f5234554`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 87 B |
| Entropía | 4.9 |
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
| hash | c660b6b192a0702f8f324e9a281f11ed0d687d1eb0bc209ad40945ccafc8d958 | static_analysis |
| ip | 172.110.223.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
