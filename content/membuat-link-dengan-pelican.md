Title: Membuat Link Ke Konten Internal dan Konten Static Dengan Pelican
Date: 2016-12-24 15:54
Category: Python
Tags: pelican, linking, internal, content, file, image
Slug: membuat-link-dengan-pelican
Authors: Yanwar Solahudin
Summary: Membahas bagaimana caranya membuat link dengan pelican


Beberapa posting terkadang memiliki link ke halaman lain baik itu berupa anchor atau semacam resource image (gambar) atau file. di sini kita akan belajar bagaimana menghubungkan konten lain (internal content) dengan link di pelican dan belajar juga bagaimana menghubungkan konten statis lain seperti gambar atau file dengan link di pelican.

## Link Konten Internal

asumsikan di dalam direktori `content` kita memiliki strukur direktori berikut:

```
myblogs/
├── content
│   ├── kategori/
│   │   └── artikel1.md
│   ├── artikel2.md
│   └── halaman
│       └── tentang.md
└── .....
```

selanjutnya pada file `artikel2.md` asumsikan kita memiliki isi sebagai berikut:

```markdown
Title: Artikel ke dua
Date: 2016-12-24 10:02

Contoh menggunakan link pada pelican.

[link 1]({filename}kategory/artikel1.md)
[link 2]({filename}/kategori/artikel1.md)
```

Terdapat dua link, dimana `link 1` merupakan link relatif ke file saat ini sedangkan pada `link 2` merupakan link relatif terhadap root content.

## Link Konten Static

Selain link ke konten internal, kita juga akan belajar bagaimana menampilkan link file atau image dengan pelican. asumsikan kita memiliki struktur direktori content berikut:

```
content
├── images
│   └── foto.jpg
├── pdfs
│   └── bagan.pdf
└── pages
    └── test.md
```

pada file `test.md` berisi:

```markdown
![Foto]({filename}/images/foto.jpg)
[Bagan]({filename}/pdfs/bagan.pdf)
```

pada bagian `![Foto]` berisi link untuk menampilkan file `foto.jpg` yang ada di dalam direktori `content/images/foto.jpg`. sedangkan pada bagian `[Bagan]` berisi link untuk file `bagan.pdf` yang ada di dalam direktori `content/pdfs/bagan.pdf`. 

Selanjutnya, buka file `pelicanconf.py` dan tambahkan bagian kode berikut untuk memberitahu pelican bahwa direktori `images` dan `pdfs` merupakan file static agar saat merender content, pelican akan membuat link ke file-file di dalam direktori tersebut.

```Python
STATIC_PATHS = ['images', 'pdfs']
```

