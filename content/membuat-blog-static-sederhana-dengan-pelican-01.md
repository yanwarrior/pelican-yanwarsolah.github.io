Title: Membuat Blog Static Sederhana Dengan Pelican (Part 1)
Date: 2016-12-23 10:56
Modified: 2016-12-23 13:53
Category: Python
Tags: python 3, static blog, pelican
Slug: membuat-blog-static-sederhana-dengan-pelican-1
Authors: Yanwar Solahudin
Summary: Bagaimana membuat blog static sederhana dengan pelican.

Blog static pada dasarnya memang sama dengan blog-blog yang kita lihat pada umumnya seperti wordpress, blogger dll. namun perbedaan mencolok dengan blog-blog pada umumnya adalah blog static hanya menyimpan tulisan dalam bentuk file based dan tidak menggunakan database seperti MySQL atau database lainnya untuk menyimpan tulisan kita. 

Blog static membutuhkan tools untuk menggenerate apa yang kita tulis (dalam format tertentu) menjadi bentuk yang dapat dibaca oleh browser yakni file `html`. biasanya setiap tools memberikan format penulisan yang berbeda-beda. tapi pada umumnya format penulisan yang digunakan menggunakan format `markdown`. 

Pada tutorial ini, kita akan membuat blog static sederhana menggunakan `pelican`. pelican merupakan package `Python` yang dapat kita gunakan untuk membuat blog static seperti halnya `jekyll`. 

## Instalasi Pelican

karena pelican merupakan package Python, sudah pasti membutuhkan Python untuk menjalankan tools ini maka di sini saya asumsikan kita sudah menginstal Python.

Pada command line, ketik perintah berikut:

```
pip install pelican
```

Selanjutnya, ketik perintah berikut ini untuk membuat setup baru untuk blog static yang ingin kita buat:

```
pelican-quickstart
```

setelah kita menjalankan perintah diatas. kita akan disuguhi pertanyaan. untuk saat ini, jawab saja pertanyaan-pertanyaan secara default (dengan menekan tombol enter).

```
> Where do you want to create your new web site? [.] myblogs
> What will be the title of this web site? My Blog
> Who will be the author of this web site? Yanwar Solahudin
> What will be the default language of this web site? [en] en
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n) Y
> How many articles per page do you want? [10] 10
> What is your time zone? [Europe/Paris] Asia/Jakarta
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) Y
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) Y
> Do you want to upload your website using FTP? (y/N) N
> Do you want to upload your website using SSH? (y/N) N
> Do you want to upload your website using Dropbox? (y/N) N
> Do you want to upload your website using S3? (y/N) N
> Do you want to upload your website using Rackspace Cloud Files? (y/N) N
> Do you want to upload your website using GitHub Pages? (y/N) N

Done. Your new project is available at D:\Yanwar Solahudin\latihan\myblog\myblogs
```

setelah selesai menjawab pertanyaan, kita memiliki struktur proyek seperti berikut:

```
myblogs/
├── content
│   └── (pages)
├── output
├── develop_server.sh
├── fabfile.py
├── Makefile
├── pelicanconf.py
└── publishconf.py
```

berikut ini adalah penjelasan beberapa direktori dan file-file penting dari struktur proyek di atas:

* `content`: direktori ini adalah direktori tempat menyimpan semua file-file content yang akan kita buat dengan format markdown (bisa juga dengan format rst).
* `output`: direktori ini adalah direktori tempat menyimpan semua file-file output hasil generate pelican menjadi file statis dalam format html. di dalam direktori inilah file-file yang bisa kita upload ke hosting.
* `pelicanconf.py`: adalah file konfigurasi dimana di dalam file ini kita bisa mengatur proyek blog static kita, misalnya kita bisa mengatur judul blog, mengatur themes yang digunakan dan lain sebagainya.

## Membuat Content Pertama

Sebelum menjalankan server pelican, pastikan kita sudah memiliki file konten di dalam direktori `content`. buat file bernama `myfirst-content.md` dan isi file tersebut dengan format seperti ini:

```markdown
Title: Kontent pertama saya
Date: 2012-12-22 10:20
Modified: 2012-12-23 19:30
Category: Python
Tags: pelican, belajar, nulis
Slug: konten-pertama-saya
Authors: Yanwar Solahudin
Summary: Ini adalah konten pertama saya yang saya tulis dengan markdown

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
```

* pada bagian `Title` berisi judul postingan kita.
* pada bagian `Date` berisi tanggal kita posting.
* pada bagian `Modified` berisi tanggal kita merubah konten postingan kita. ini sifatnya opsional, karena pertama kali tulisan dibuat, bagian field ini tidak perlu disertakan.
* pada bagian `Category` berisi nama kategori untuk tulisan yang kita buat. nilainya bisa berisi lebih dari satu kategori, tapi menurut saya isikan nilainya hanya satu kategori yang unik saja.
* pada bagian `Tags` berisi tag-tag untuk tulisan yang kita buat, nilainya pun bisa lebih dari satu tag.
* pada bagian `Slug` berisi slug untuk URL pada posting kita. slug ini akan berdampingan dengan URL untuk mengakses link pada posting kita. isinya harus unik.
* pada bagian `Authors` berisi nama penulisnya. silahkan isi nama anda dibagian field ini.
* pada bagian `Summary` berisi ringkasan dari apa yang kita tulis.

Setelah kita membuat konten pertama, selanjutnya ketik perintah di bawah ini untuk menggenerate content menjadi file `html` yang nantinya file html tersebut akan disimpan ke dalam direktori `output`. pertama-tama, masuk dulu ke dalam direktori `myblogs`.


```
cd myblogs
pelican content
```

Sekarang coba cek ke dalam direktori `output`, kita akan melihat beberapa file html yang sudah digenerate oleh pelican.


```
output/
│   archives.html
│   authors.html
│   categories.html
│   index.html
│   konten-pertama-saya.html
│   tags.html
│
├───author
│       yanwar-solahudin.html
│
├───category
│       python.html
│
├───feeds
│       all-en.atom.xml
│       all.atom.xml
│       python.atom.xml
│       yanwar-solahudin.atom.xml
│       yanwar-solahudin.rss.xml
│
├───tag
│       belajar.html
│       nulis.html
│       pelican.html
│
└───theme
    ├───css
    │       main.css
    │       pygment.css
    │       reset.css
    │       typogrify.css
    │       wide.css
    │
    └───images
        └───icons
                aboutme.png
                bitbucket.png
                delicious.png
                facebook.png
                github.png
                gitorious.png
                gittip.png
                google-groups.png
                google-plus.png
                hackernews.png
                lastfm.png
                linkedin.png
                reddit.png
                rss.png
                slideshare.png
                speakerdeck.png
                stackoverflow.png
                twitter.png
                vimeo.png
                youtube.png
```

Sekarang, jalankan server pelican. masuk dulu ke dalam direktori `output` dengan perintah `cd output` lalu ketik perintah di bawah ini:

```
python -m pelican.server
```

Buka browser lalu akses ke alamat `http://localhost:8000/`. dan hasilnya seperti ini:

![Alt Text]({filename}/images/pelicanku.jpg)



