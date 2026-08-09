# 🧬 Payload Analysis

`79d84cf0a90c43031c22ff88bdd1b1ef4cb29121ff76a1321f382e9b98bd75de`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida. Se asociaron 2 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `79d84cf0a90c43031c22ff88bdd1b1ef4cb29121ff76a1321f382e9b98bd75de`
- **MD5:** `2ec2f6b730ede5b7267eaab518f8c316`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 3.0 KiB |
| Entropía | 7.7 |
| Strings | 15 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.7; iocs=3

## 🖥️ Comandos observados / extraídos

```text
/data/local/tmp/tv.apk,33261DATA
/data/local/tmp/tv.apkOKAY
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 79d84cf0a90c43031c22ff88bdd1b1ef4cb29121ff76a1321f382e9b98bd75de | static_analysis |
| command | /data/local/tmp/tv.apk,33261DATA | strings |
| command | /data/local/tmp/tv.apkOKAY | strings |
| ip | 1.28.208.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
