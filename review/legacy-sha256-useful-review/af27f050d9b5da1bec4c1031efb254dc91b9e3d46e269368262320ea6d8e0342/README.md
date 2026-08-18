# 🧬 Payload Analysis

`af27f050d9b5da1bec4c1031efb254dc91b9e3d46e269368262320ea6d8e0342`

## 📌 Resumen

Artefacto de 279 B. Entropía registrada: 4.89. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:07:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `af27f050d9b5da1bec4c1031efb254dc91b9e3d46e269368262320ea6d8e0342`
- **SHA1:** `9100aa9cdd9bd8efd657a721c662de1f523d3677`
- **MD5:** `fd5ec00a138e0db6c294f24c9ec70980`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 279 B |
| Entropía | 4.89 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🖥️ Comandos observados / extraídos

```text
>/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev/shm;>/tmp/.x&&cd /
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev/shm;>/tmp/.x&&cd / | strings |
| hash | af27f050d9b5da1bec4c1031efb254dc91b9e3d46e269368262320ea6d8e0342 | static_analysis |
| ip | 153.117.37.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
