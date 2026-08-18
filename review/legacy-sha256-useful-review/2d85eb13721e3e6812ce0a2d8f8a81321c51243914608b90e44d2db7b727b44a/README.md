# 🧬 Payload Analysis

`2d85eb13721e3e6812ce0a2d8f8a81321c51243914608b90e44d2db7b727b44a`

## 📌 Resumen

Artefacto de 206 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.37. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 4 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:23:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2d85eb13721e3e6812ce0a2d8f8a81321c51243914608b90e44d2db7b727b44a`
- **SHA1:** `fc7b9d05e73e0f6a6d44f5bb964251757a8744a2`
- **MD5:** `c1a7d7623caf77b590ee7e0b333e2399`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 206 B |
| Entropía | 5.37 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /var/.env HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 136.0.0.XXX | static_analysis |
| ip | 190.179.128.XXX | static_analysis |
| command | GET /var/.env HTTP/1.1 | strings |
| hash | 2d85eb13721e3e6812ce0a2d8f8a81321c51243914608b90e44d2db7b727b44a | static_analysis |
| ip | 52.200.76.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
