# 🧬 Payload Analysis

`e577d7c31a35b3e2d19d217f013ecaadd6e8ce262099452d928d9c4ebc2b72dc`

## 📌 Resumen

Artefacto de 1.1 KiB. Entropía registrada: 5.32. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:01:00.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e577d7c31a35b3e2d19d217f013ecaadd6e8ce262099452d928d9c4ebc2b72dc`
- **SHA1:** `36e5a98f89507931a2e12dcc486680dd5ba353b2`
- **MD5:** `46b861c214ebbc9bdc17b5848869f480`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.1 KiB |
| Entropía | 5.32 |
| Strings | 25 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🖥️ Comandos observados / extraídos

```text
[4lcuadmin@OpenWrt:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | [4lcuadmin@OpenWrt:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd / | strings |
| hash | e577d7c31a35b3e2d19d217f013ecaadd6e8ce262099452d928d9c4ebc2b72dc | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
