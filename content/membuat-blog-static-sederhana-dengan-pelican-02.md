Title: Membuat Blog Static Sederhana Dengan Pelican (Part 2)
Date: 2016-12-23 21:47
Category: Python
Tags: python 3, static blog, pelican
Slug: membuat-blog-static-sederhana-dengan-pelican-2
Authors: Yanwar Solahudin
Summary: Bagaimana membuat blog static sederhana dengan pelican.

Melanjutkan postingan sebelumnya tentang [membuat blog static sederhana]({filename}/membuat-blog-static-sederhana-dengan-pelican-01.md) dengan pelican. pada tutorial ini, kita akan belajar bagaimana mengganti themes pada pelican.

## Instalasi Themes
Untuk melihat-lihat themes pelican, akses link berikut [pelican themes](http://www.pelicanthemes.com/). misalnya kita pilih saja themes `iris` yang bisa kita peroleh dengan cara clone dari repositori `iris` di url github [ini](https://github.com/slok/iris). di dalam direktori `myblogs`, buat direktori bernama `themes`:

```
mkdir themes
```

selanjutnya, masuk ke dalam direktori `themes`:

```
cd themes
```

lakukan clone dari repositori `iris`:

```
git clone https://github.com/slok/iris.git
```

oke, setelah kita selesai clone, di dalam command line, keluar dari direktori `themes` (berada di dalam direktori `myblogs`). selanjutnya buka file `pelicanconf.py` dan tambahkan kode berikut ini:

```python
THEME = 'iris'
```

setelah itu, ketik perintah di bawah ini untuk menginstal themes iris pada pelican:

```
pelican-themes --install themes/iris
```

untuk mengecek apakah themes `iris` sudah terinstal, ketik:

```
pelican-themes --list
```

perintah di atas akan menampilkan daftar-daftar tema yang terinstal pada pelican. langkah selanjutnya, lakukan generate ulang dengan perintah:

```
pelican content
```

Setelah selesai, masuk ke direktori `output` dan jalankan server pelican:

```
cd output
python -m pelican.server
```

buka browser dan ketik url `http://127.0.0.1:8000`, dan tralaaa hasilnya sudah berubah dengan tampilan tema `iris`:

![Alt Text]({filename}/images/iris.jpg)








