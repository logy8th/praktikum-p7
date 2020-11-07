# Tugas Pertemuan ke-7 [Senin 02-10-2020]
- ***Simpan project Praktikum hari ini ke repository***
- ***Buat penjelasan setiap Lab/Latihannya pada file README.md***
<br>
<pre>
Nama    : Naufal Nirwansyah 
Kelas   : TI.20.A1
NIM     : 312010174
Dosen   : Agung Nugroho S.Kom, M.Kom
</pre>

# Latihan 1
<br>
Pada Pertemuan ke-7 kemarin, saya mendapat tugas dari Dosen Bahasa Pemrograman, Bapak. Agung Nugroho,S.Kom.,M.Kom. <br>
Dan pada 'Latihan 1' ini saya diminta untuk membuat program dengan perulangan bertingkat (nested).

**Dibawah ini adalah latihan yang diberikan oleh Dosen :**<br>

![latihan1](latihan1/task.png)
<br>
<br>
Untuk membuat program dengan input seperti diatas, saya menggunakan source code sebagai berikut: <br>

```
for row in range(0, 10):
    for col in range(0, 10):
        num = row + col
        if num < 10:
            empty = "  "
        else:
            if num < 100:
                empty  = " "
        print(empty, num, end = '')
    print()
```
<br>

**Source code diatas akan muncul result sebagai berikut:** <br>

![Lat1](latihan1/lat1.png) <br>
