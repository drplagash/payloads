# 🧬 Payload Analysis

`843c37a49cb17921e3b9e809e67a21cf588fc550877be4ee5026236bc3dd2ad4`

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

- **SHA256:** `843c37a49cb17921e3b9e809e67a21cf588fc550877be4ee5026236bc3dd2ad4`
- **MD5:** `d973353a648689f63eacb69f81c4e5dd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 3.1 KiB |
| Entropía | 7.7 |
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
| hash | 843c37a49cb17921e3b9e809e67a21cf588fc550877be4ee5026236bc3dd2ad4 | static_analysis |
| ip | 180.105.74.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
