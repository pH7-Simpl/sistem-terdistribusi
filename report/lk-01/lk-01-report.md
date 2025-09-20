# LK 01: Lingkungan Praktik Mandiri + Ujicoba Messaging Protocols ([Brone](https://brone.ub.ac.id/mod/assign/view.php?id=124118))
- Referensi https://github.com/abazh/dist_sys

1. Buat Lingkungan Praktik Mandiri berbasis VSCode+GitHub Copilot, WSL2 + Ubuntu, Docker Container
2. Fork Repository Program: https://github.com/abazh/dist_sys ke dalam akun Github anda
3. Lakukan ujicoba per protocol dan modifikasi yang diperlukan
4. Buat laporannya dalam respository akun Github anda (bisa private/tidak harus public)
5. Invite akun abazh@ub.ac.id ke repository anda.
6. Submit link ke repository anda ke Tugas ini.

# Report
## 1. Ujicoba REST
1. Mengikuti langkah - langkah yang ada pada Instruksi. \
![rest-instruction](src/1.png)
- Hasil mengikuti Instruksi
    1. Menjalankan perintah:
        ```
        docker compose -f compose/rest.yml up -d
        ```
        ![rest-command-1](src/2.png)
    2. Menjalankan perintah:
        ```
        docker compose -f compose/rest.yml exec rest-server python server.py
        ```
        ![rest-command-2](src/3.png)
    3. Menjalankan perintah:
        ```
        docker compose -f compose/rest.yml exec rest-client python client.py --op both -a 2 -b 3
        ```
        ![rest-command-3](src/4.png)

2. Memodifikasi source code
    1. Mengubah client.py
        1. Menambahkan fungsi call_calc(expr) \
        ![modified-client.py-1](src/5.png)
        2. Memodifikasi main function \
        ![modified-client.py-2](src/6.png)
    2. Mengubah server.py
        1. Import sympy \
        ![modified-server.py-1](src/7.png)
        2. Menambahkan fungsi calc_expression \
        ![modified-server.py-2](src/8.png)
    3. mengubah requirement.txt
        1. Menambahkan sympy kedalam library \
        ![modified-requirement.txt-1](src/9.png)

3. Menjalankan source code yang sudah termodifikasi
    1. Menjalankan perintah:
        ```
        docker compose -f compose/rest.yml up -d
        ```
        ![rest-modified-command-1](src/10.png)
    2. Menjalankan perintah:
        ```
        docker compose -f compose/rest.yml exec rest-server python server.py
        ```
        ![rest-modified-command-2](src/11.png)
    3. Menjalankan perintah:
        ```
        docker compose -f compose/rest.yml exec rest-client python client.py --op calc --expr "(10/2)+7*3"
        ```
        ![rest-modified-command-3](src/12.png)


## 2. Ujicoba Reqresp
1. Mengikuti langkah - langkah yang ada pada Instruksi. \
![reqresp-instruction](src/13.png)
- Hasil mengikuti instruksi
    1. Menjalankan perintah:
        ```
        docker compose -f compose/reqresp.yml up -d
        ```
        ![rest-command-1a](src/14.png) \
        ![rest-command-1b](src/15.png)
    2. Menjalankan perintah:
        ```
        docker compose -f compose/reqresp.yml exec reqresp-server python server.py
        ```
        ![rest-command-2](src/16.png)
    3. Menjalankan perintah:
        ```
        docker compose -f compose/reqresp.yml exec reqresp-client python client.py
        ```
        ![rest-command-3](src/17.png)
    4. Mencoba tcp reqresp \
    ![try-reqresp-1](src/18.png)
    5. Mencoba tcp reqresp dengan dibaca tcp-dump \
    ![try-reqresp-2](src/19.png)
    6. Mencoba tcp reqresp dibaca tcp-dumb dan wireshark \
    ![try-reqresp-3](src/20.png) \
    ![try-reqresp-3](src/21.png) \
    ![try-reqresp-3](src/22.png)

## 3. Ujicoba JSON-RPC
1. Mengikuti langkah - langkah yang ada pada Instruksi. \
![json-rpc-instruction](src/23.png)
- Hasil mengikuti instruksi
    1. Menjalankan perintah:
        ```
        docker compose -f compose/rpc.yml up -d
        ```
        ![json-rpc-command-1](src/24.png)
    2. Menjalankan perintah:
        ```
        docker compose -f compose/rpc.yml exec rpc-server python rpcserver.py
        ```
        ![json-rpc-command-2](src/25.png)
    3. Menjalankan perintah:
        ```
        docker compose -f compose/rpc.yml exec rpc-client python rpcclient.py
        ```
        ![json-rpc-command-3](src/26.png)

2. Memodifikasi source code
    1. mengubah requirement.txt \
    ![json-rpc-modified-requirement.txt-1](src/27.png)
    2. Mengubah rpcserver.py
        1. Menambahkan fungsi calc(expr: str) \
        ![json-rpc-modified-rpcserver.py-1](src/28.png)
    3. Mengubah rpcclient.py
        1. Menambahkan panggilan operasi kalkulasi bebas \
        ![json-rpc-modified-rpcclient.py-1](src/29.png)

3. Menjalankan source code yang sudah termodifikasi
    1. Menjalankan perintah:
        ```
        docker compose -f compose/rpc.yml up -d
        ```
        ![json-rpc-modified-command-1](src/30.png)
    2. Menjalankan perintah:
        ```
        docker compose -f compose/rpc.yml exec rpc-server python rpcserver.py
        ```
        ![json-rpc-modified-command-2](src/31.png)
    3. Menjalankan perintah:
        ```
        docker compose -f compose/rpc.yml exec rpc-client python rpcclient.py
        ```
        ![json-rpc-modified-command-3](src/32.png)

## 4. Ujicoba SOAP
1. Mengikuti langkah - langkah yang ada pada Instruksi. \
![soap-instruction](src/33.png)
- Hasil mengikuti Instruksi
    1. Menjalankan perintah:
        ```
        docker compose -f compose/soap.yml up -d
        ```
        ![soap-command-1](src/34.png)
    2. Menjalankan perintah:
        ```
        docker compose -f compose/soap.yml exec soap-server python server.py
        ```
        ![soap-command-2](src/35.png)
    3. Menjalankan perintah:
        ```
        docker compose -f compose/soap.yml exec soap-client python client.py
        ```
        ![soap-command-3](src/36.png)

2. Memodifikasi source code
    1. Mengubah server.py
        1. Menambahkan import sympy dan menambahkan Unicode dan Double dari spyne \
        ![modified-soap-client.py-1](src/37.png)
        2. Menambahkan fungsi kalkulasi bebas pada kelas CalculatorService \
        ![modified-soap-client.py-2](src/38.png)
    2. Mengubah client.py
        1. Menambahkan pengujian kalkulasi bebas (2 kalkulasi) \
        ![modified-soap-server.py-1](src/39.png)
    3. mengubah requirement.txt
        1. Menambahkan sympy kedalam library \
        ![modified-soap-requirement.txt-1](src/40.png)

3. Menjalankan source code yang sudah termodifikasi
    1. Menjalankan perintah:
        ```
        docker compose -f compose/soap.yml up -d
        ```
        ![soap-modified-command-1](src/41.png)
    2. Menjalankan perintah:
        ```
        docker compose -f compose/soap.yml exec soap-server python server.py
        ```
        ![soap-modified-command-2](src/42.png)
    3. Menjalankan perintah:
        ```
        docker compose -f compose/soap.yml exec soap-client python client.py
        ```
        ![soap-modified-command-3](src/43.png)

## 5. Ujicoba MQTT
1. Mengikuti langkah - langkah yang ada pada Instruksi. \
![mqtt-instruction](src/44.png)
- Hasil mengikuti Instruksi
    1. Menjalankan perintah:
        ```
        docker compose -f compose/mqtt.yml up -d
        ```
        ![mqtt-command-1](src/45.png)
    2. Menjalankan perintah:
        ```
        docker compose -f compose/mqtt.yml exec mqtt-sub python sub.py
        ```
        ![mqtt-command-2](src/46.png)
    3. Menjalankan perintah:
        ```
        docker compose -f compose/mqtt.yml exec mqtt-pub python pub.py
        ```
        ![mqtt-command-3](src/47.png)

## 6. Ujicoba UDP One-way
1. Mengikuti langkah - langkah yang ada pada Instruksi. \
![udp-oneway-instruction](src/48.png)
- Hasil mengikuti Instruksi
    1. Menjalankan perintah:
        ```
        docker compose -f compose/udp.yml up -d
        ```
        ![udp-oneway-command-1](src/49.png)
    2. Menjalankan perintah:
        ```
        docker compose -f compose/udp.yml exec udp-server python serverUDP.py
        ```
        ![udp-oneway-command-2](src/50.png)
    3. Menjalankan perintah:
        ```
        docker compose -f compose/udp.yml exec udp-client python clientUDP.py
        ```
        ![udp-oneway-command-3](src/51.png)

2. Memodifikasi source code
    1. Mengubah clientUDP.py
        1. Menambahkan pesan ektra kepada server \
        ![modified-udp-oneway-clientUDP.py-1](src/52.png)

3. Menjalankan source code yang sudah termodifikasi
    1. Menjalankan perintah:
        ```
        docker compose -f compose/udp.yml up -d
        ```
        ![udp-oneway-modified-command-1](src/53.png)
    2. Menjalankan perintah:
        ```
        docker compose -f compose/udp.yml exec udp-server python serverUDP.py
        ```
        ![udp-oneway-modified-command-2](src/54.png)
    3. Menjalankan perintah:
        ```
        docker compose -f compose/udp.yml exec udp-client python clientUDP.py
        ```
        ![udp-oneway-modified-command-3](src/55.png)