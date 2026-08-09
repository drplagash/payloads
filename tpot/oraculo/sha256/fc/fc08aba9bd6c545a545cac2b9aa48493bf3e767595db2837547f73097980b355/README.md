# 🧬 Payload Analysis

`fc08aba9bd6c545a545cac2b9aa48493bf3e767595db2837547f73097980b355`

## 📌 Resumen

Artefacto de 3.1 KiB. La evidencia estática disponible identifica capacidad de descarga remota. Se observaron o extrajeron 2 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:44:08.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fc08aba9bd6c545a545cac2b9aa48493bf3e767595db2837547f73097980b355`
- **MD5:** `a7a8c347af2c52820fc20f3aa364db6e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 3.1 KiB |
| Entropía | 7.71 |
| Strings | 14 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Alta entropía / posible empaquetado o cifrado**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp); High entropy (7.7) — posible packer/encrypted

## 🖥️ Comandos observados / extraídos

```text
/data/local/tmp/ufo.apkOKAY
/data/local/tmp/ufo.apk,33261DATA
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | /data/local/tmp/ufo.apkOKAY | strings |
| command | /data/local/tmp/ufo.apk,33261DATA | strings |
| hash | fc08aba9bd6c545a545cac2b9aa48493bf3e767595db2837547f73097980b355 | static_analysis |
| ip | 180.105.74.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
