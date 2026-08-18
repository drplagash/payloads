# 🧬 Payload Analysis

`7e4d651a182f046579ae4224b4db72382ded079e5a955714af5fc08808540170`

## 📌 Resumen

Artefacto de 145 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.13. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:39:05.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7e4d651a182f046579ae4224b4db72382ded079e5a955714af5fc08808540170`
- **SHA1:** `52536b05f99d354a8aa9a53051615fb23c39c858`
- **MD5:** `7b38aaf17e0d8d6385515478a0f1e921`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 145 B |
| Entropía | 5.13 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/8.7.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.166.XXX | static_analysis |
| command | User-Agent: curl/8.7.1 | strings |
| hash | 7e4d651a182f046579ae4224b4db72382ded079e5a955714af5fc08808540170 | static_analysis |
| ip | 178.128.151.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
