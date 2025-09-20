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
    1. Menjalankan perintah docker compose -f compose/rest.yml up -d
    ![rest-command-1](src/2.png)
    2. Menjalankan perintah docker compose -f compose/rest.yml exec rest-server python server.py
    ![rest-command-2](src/3.png)
    3. Menjalankan perintah docker compose -f compose/rest.yml exec rest-client python client.py --op both -a 2 -b 3
    ![rest-command-3](src/4.png)

2. Memodifikasi source code
    1. Mengubah client.py
        1. Menambahkan fungsi call_calc(expr) \
        ![modificate-client.py-1](src/5.png)
        2. Memodifikasi main function \
        ![modificate-client.py-2](src/6.png)
    2. Mengubah server.py
        1. Import sympy \
        ![modificate-server.py-1](src/7.png)
        2. Menambahkan fungsi calc_expression \
        ![modificate-server.py-2](src/8.png)
    3. mengubah requirement.txt
        1. Menambahkan sympy kedalam library \
        ![modificate-requirement.txt-1](src/9.png)

3. Menjalankan source code yang sudah termodifikasi
    1. Menjalankan perintah docker compose -f compose/rest.yml up -d
    ![rest-modified-command-1](src/10.png)
    2. Menjalankan perintah docker compose -f compose/rest.yml exec rest-server python server.py
    ![rest-modified-command-2](src/11.png)
    3. Menjalankan perintah docker compose -f compose/rest.yml exec rest-client python client.py --op calc --expr "(10/2)+7*3"
    ![rest-modified-command-3](src/12.png)


## 2. Ujicoba Reqresp
1. Mengikuti langkah - langkah yang ada pada Instruksi. \
![reqresp-instruction](src/13.png)
- Hasil mengikuti instruksi
    1. Menjalankan perintah docker compose -f compose/reqresp.yml up -d \
    ![rest-command-1a](src/14.png)
    ![rest-command-1b](src/15.png)
    2. Menjalankan perintah docker compose -f compose/reqresp.yml exec reqresp-server python server.py \
    ![rest-command-2](src/16.png)
    3. Menjalankan perintah docker compose -f compose/reqresp.yml exec reqresp-client python client.py \
    ![rest-command-3](src/17.png)
    4. Mencoba tcp reqresp \
    ![try-reqresp-1](src/18.png)
    5. Mencoba tcp reqresp dengan dibaca tcp-dump \
    ![try-reqresp-2](src/19.png)
    6. Mencoba tcp reqresp dibaca tcp-dumb dan wireshark \
    ![try-reqresp-3](src/20.png)
    ![try-reqresp-3](src/21.png)
    ![try-reqresp-3](src/22.png)