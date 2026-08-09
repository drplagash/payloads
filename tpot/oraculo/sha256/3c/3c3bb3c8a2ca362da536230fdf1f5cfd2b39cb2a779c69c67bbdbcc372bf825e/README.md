# 🧬 Payload Analysis

`3c3bb3c8a2ca362da536230fdf1f5cfd2b39cb2a779c69c67bbdbcc372bf825e`

## 📌 Resumen

Artefacto de 858 B. Entropía registrada: 5.46. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3c3bb3c8a2ca362da536230fdf1f5cfd2b39cb2a779c69c67bbdbcc372bf825e`
- **SHA1:** `e3aea97cfc8277d6715d513191e0ad486ddd27f1`
- **MD5:** `f8c03079dc3c27f2372d57ffc2784f2a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 858 B |
| Entropía | 5.46 |
| Strings | 21 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🖥️ Comandos observados / extraídos

```text
[4lservice@DIR-859:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | [4lservice@DIR-859:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd / | strings |
| hash | 3c3bb3c8a2ca362da536230fdf1f5cfd2b39cb2a779c69c67bbdbcc372bf825e | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
