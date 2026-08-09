# 🧬 Payload Analysis

`14802b907cc9f839b393c45ab8e1d6dcb9285a8724b2832714a001df6560f98b`

## 📌 Resumen

Artefacto de 187 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.28. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `14802b907cc9f839b393c45ab8e1d6dcb9285a8724b2832714a001df6560f98b`
- **SHA1:** `54d2d71254d2484bbe4152aebdd2ed8e404f3364`
- **MD5:** `ed6e811886838b286c4c7185a39270ef`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 187 B |
| Entropía | 5.28 |
| Strings | 7 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/8
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | User-Agent: curl/8 | strings |
| hash | 14802b907cc9f839b393c45ab8e1d6dcb9285a8724b2832714a001df6560f98b | static_analysis |
| ip | 103.176.111.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
