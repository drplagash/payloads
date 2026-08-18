# 🧬 Payload Analysis

`a969dd9e6af7c82745eaf60bf14fe28bb187028e7dc965e218af6bef6318d6b7`

## 📌 Resumen

Artefacto de 1.1 KiB. Entropía registrada: 5.32. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T18:39:48.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a969dd9e6af7c82745eaf60bf14fe28bb187028e7dc965e218af6bef6318d6b7`
- **MD5:** `44556a673987005e5f7e8a6026aed9f5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.1 KiB |
| Entropía | 5.32 |
| Strings | 25 |

## 🖥️ Comandos observados / extraídos

```text
[4lroot@OpenWrt:~# >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | [4lroot@OpenWrt:~# >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev | strings |
| hash | a969dd9e6af7c82745eaf60bf14fe28bb187028e7dc965e218af6bef6318d6b7 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
