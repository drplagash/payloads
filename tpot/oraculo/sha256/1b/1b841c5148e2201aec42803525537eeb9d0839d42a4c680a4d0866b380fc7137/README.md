# 🧬 Payload Analysis

`1b841c5148e2201aec42803525537eeb9d0839d42a4c680a4d0866b380fc7137`

## 📌 Resumen

Artefacto de 294 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.19. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Ejecución. Se identificaron 3 comandos observados o extraídos. Se identificaron 5 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1b841c5148e2201aec42803525537eeb9d0839d42a4c680a4d0866b380fc7137`
- **MD5:** `e638811342edc05cec371fd69ff2d2e5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 294 B |
| Entropía | 5.19 |
| Strings | 12 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /bins/busywget.sh HTTP/1.1
User-Agent: curl/7.73.0
GET /bins/wget.sh HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 64.89.163.XXX | static_analysis |
| command | GET /bins/busywget.sh HTTP/1.1 | strings |
| command | User-Agent: curl/7.73.0 | strings |
| command | GET /bins/wget.sh HTTP/1.1 | strings |
| hash | 1b841c5148e2201aec42803525537eeb9d0839d42a4c680a4d0866b380fc7137 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
