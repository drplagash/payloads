# 🧬 Payload Analysis

`802cf9dd44666c4130f1444092b834c39a541dc0b27381345e6a0df6eed31008`

## 📌 Resumen

Artefacto de 279 B. Entropía registrada: 5.02. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:43:29.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `802cf9dd44666c4130f1444092b834c39a541dc0b27381345e6a0df6eed31008`
- **MD5:** `50a7034bac7ecd3a2aff58ae6cedf356`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 279 B |
| Entropía | 5.02 |
| Strings | 6 |

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
| hash | 802cf9dd44666c4130f1444092b834c39a541dc0b27381345e6a0df6eed31008 | static_analysis |
| ip | 223.123.124.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
