# 🧬 Payload Analysis

`2a51602a906704a6cf2986bcc641fc17c6378773898ebaffaa99059ba0cae3c4`

## 📌 Resumen

Artefacto de 145 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.16. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:24:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2a51602a906704a6cf2986bcc641fc17c6378773898ebaffaa99059ba0cae3c4`
- **SHA1:** `c3f23433d5c4ba2c0ed4d15207af29d01b2fca91`
- **MD5:** `b07c825b2b83e9796dfb5f0bc65119d1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 145 B |
| Entropía | 5.16 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.73.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 176.65.139.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| hash | 2a51602a906704a6cf2986bcc641fc17c6378773898ebaffaa99059ba0cae3c4 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
