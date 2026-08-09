# 🧬 Payload Analysis

`82b49fc669d404515a56131062777f0ec6d4c5f579f5730d26413cbbf22d123d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `82b49fc669d404515a56131062777f0ec6d4c5f579f5730d26413cbbf22d123d`
- **SHA1:** `0af97d03df620ab45471c929e7268437a70c2639`
- **MD5:** `85c0fbf4ba7a0d335532e16b4a02207e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 274 B |
| Entropía | 4.97 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🖥️ Comandos observados / extraídos

```text
>/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev/shm;>/tmp/.x&&cd /
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 82b49fc669d404515a56131062777f0ec6d4c5f579f5730d26413cbbf22d123d | static_analysis |
| command | >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev/shm;>/tmp/.x&&cd / | strings |
| ip | 103.244.172.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
