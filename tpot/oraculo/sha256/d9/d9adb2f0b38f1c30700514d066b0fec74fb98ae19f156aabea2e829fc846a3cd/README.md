# 🧬 Payload Analysis

`d9adb2f0b38f1c30700514d066b0fec74fb98ae19f156aabea2e829fc846a3cd`

## 📌 Resumen

Artefacto de 2.9 KiB. Presenta entropía elevada (7.67), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 comandos observados o extraídos. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d9adb2f0b38f1c30700514d066b0fec74fb98ae19f156aabea2e829fc846a3cd`
- **SHA1:** `e0f372e8b8e4f73cadb97332ace3a167a538ceed`
- **MD5:** `50085511e0a5202f6098344011d87edb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 2.9 KiB |
| Entropía | 7.67 |
| Strings | 14 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.7; iocs=3

## 🖥️ Comandos observados / extraídos

```text
/data/local/tmp/ufo.apkOKAY0
/data/local/tmp/ufo.apk,33261DATA
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | /data/local/tmp/ufo.apkOKAY0 | strings |
| command | /data/local/tmp/ufo.apk,33261DATA | strings |
| hash | d9adb2f0b38f1c30700514d066b0fec74fb98ae19f156aabea2e829fc846a3cd | static_analysis |
| ip | 2.193.129.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
