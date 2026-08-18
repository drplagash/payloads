# 🧬 Payload Analysis

`7a3a11185b2a02f2a5aab73daf2c56b4b1a29b32be251d4cd73405015531116b`

## 📌 Resumen

Artefacto de 1.0 KiB. Entropía registrada: 5.32. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:27:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7a3a11185b2a02f2a5aab73daf2c56b4b1a29b32be251d4cd73405015531116b`
- **MD5:** `60676ff12170298e6af8a4835f5fbe8f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.0 KiB |
| Entropía | 5.32 |
| Strings | 25 |

## 🖥️ Comandos observados / extraídos

```text
[4lftp@OpenWrt:/$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev/
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | [4lftp@OpenWrt:/$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev/ | strings |
| hash | 7a3a11185b2a02f2a5aab73daf2c56b4b1a29b32be251d4cd73405015531116b | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
